import dataclasses
from typing import Any, Dict, List, Tuple, Type, Union

from ml_orchestrator.comp_protocol.comp_protocol import ComponentProtocol
from ml_orchestrator.utils.field_utils import get_param_meta_data, get_param_meta_data_str


@dataclasses.dataclass
class _FunctionParser:
    dsl_imports = "from kfp.dsl import *\nfrom typing import *\nfrom importlib.metadata import version\n"

    @classmethod
    def get_class_def(cls, component: Union[type, ComponentProtocol]) -> type:
        is_class_def = isinstance(component, type)
        com_class = component if is_class_def else component.__class__
        return com_class  # type: ignore

    @classmethod
    def comp_execute(cls, comp: Type[ComponentProtocol]) -> str:
        comp_run = "comp.execute()"
        if cls.exe_return(comp) is not None:
            comp_run = "return comp.execute()"
        return comp_run

    @classmethod
    def exe_return(cls, comp: Type[ComponentProtocol]) -> Any:
        execute_return_type = comp.execute.__annotations__.get("return")
        return execute_return_type

    @staticmethod
    def get_func_params(comp_vars: Dict[dataclasses.Field, Any], with_typing: bool = True) -> List[str]:
        with_defaults = {k: v for k, v in comp_vars.items() if v is not dataclasses.MISSING}
        without_defaults = {k: v for k, v in comp_vars.items() if v is dataclasses.MISSING}

        func_params_with = [
            get_param_meta_data_str(*get_param_meta_data(k, v), with_typing=with_typing)
            for k, v in with_defaults.items()
        ]
        func_params_without = [
            get_param_meta_data_str(*get_param_meta_data(k, v), with_typing=with_typing)
            for k, v in without_defaults.items()
        ]
        func_params = func_params_without + func_params_with

        return func_params

    @classmethod
    def comp_vars(cls, component: Type[ComponentProtocol]) -> Dict[dataclasses.Field, Any]:
        fields = dataclasses.fields(component)  # type: ignore
        ins_vars = dict()
        for field in fields:
            if not field.init:
                continue
            field_defaults = cls.parse_field_default(field)
            ins_vars[field] = field_defaults

        return ins_vars

    @classmethod
    def parse_field_default(cls, field: dataclasses.Field) -> Any:
        field_defaults = field.default if not field.default == dataclasses.MISSING else None
        field_has_default_factory = field.default_factory != dataclasses.MISSING
        field_defaults = field.default_factory() if field_has_default_factory else field_defaults  # type: ignore
        is_missing = {dataclasses.MISSING} == {field.default, field.default_factory}
        field_defaults = dataclasses.MISSING if is_missing else field_defaults
        return field_defaults

    @staticmethod
    def get_comp_params(comp_vars: Dict[dataclasses.Field, Any]) -> List[str]:
        return [f"{k.name}={k.name}" for k, v in comp_vars.items()]

    @classmethod
    def create_function(cls, component: ComponentProtocol) -> str:
        comp_class = cls.get_class_def(component)
        comp_init, func_definition = cls.get_function_parts(comp_class)
        import_compound = f"from {comp_class.__module__} import {comp_class.__name__}"
        comp_run = cls.comp_execute(comp_class)
        str_func_body = "\n\t".join([import_compound, comp_init, comp_run])
        str_func = func_definition + "\n\t" + str_func_body
        return str_func

    @classmethod
    def get_function_parts(cls, comp_class: Type[ComponentProtocol]) -> Tuple[str, str]:
        component_variables = cls.comp_vars(comp_class)
        kfp_func_name = cls.comp_func_name(comp_class)
        func_params = cls.get_func_params(component_variables)
        comp_params = cls.get_comp_params(component_variables)
        func_scope = "(\n\t" + ",\n\t".join(func_params) + (",\n)" if func_params else ")")
        comp_scope = "(\n\t\t" + ",\n\t\t".join(comp_params) + (",\n\t)" if comp_params else ")")
        return_type = ""
        if cls.exe_return(comp_class) is not None:
            return_type = f" -> {cls.exe_return(comp_class).__name__}"

        func_definition = f"def {kfp_func_name}{func_scope}{return_type}:"
        comp_init = f"comp = {comp_class.__name__}{comp_scope}"
        return comp_init, func_definition

    @classmethod
    def comp_func_name(cls, comp_class: Type[ComponentProtocol]) -> str:
        if hasattr(comp_class, "kfp_func_name"):
            return comp_class.kfp_func_name()
        func_name = comp_class.__name__
        new_func_name = cls._comp_func_name(func_name)
        return new_func_name

    @classmethod
    def _comp_func_name(cls, func_name: str) -> str:
        func_name_lower = func_name.lower()
        capital_indexes = [i for i, c in enumerate(func_name) if c.isupper()]
        new_func_name = ""
        for i, letter in enumerate(func_name_lower):
            new_func_name += "_" + letter if (i in capital_indexes and i) else letter
        return new_func_name

    @staticmethod
    def convert_to_format_str(text: str) -> str:
        new_text = text.replace(", '", ", f'").replace("['", "[f'")
        new_text = new_text.replace(', "', ', f"').replace('["', '[f"')
        return new_text

    @staticmethod
    def _get_decorator_override_params(prams: List[str]) -> List[str]:
        return [p for p in prams if "None" not in p]
