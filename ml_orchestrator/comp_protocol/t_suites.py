"""Module for component protocol test suites.

This module provides abstract test suite classes that can be extended
to test components that implement the ComponentProtocol.
"""

import abc
from typing import Any

import pytest

from .comp_protocol import ComponentProtocol
from .func_parser import FunctionParser


class ProtocolCompSuite(abc.ABC):
    """Abstract test suite for testing components that implement ComponentProtocol.

    This abstract class defines a set of tests that should be run against any
    component that implements the ComponentProtocol. Subclasses must implement
    the comp_fixture method to provide a component instance for testing.
    """

    @pytest.fixture
    @abc.abstractmethod
    def comp_fixture(self, *args: Any, **kwargs: Any) -> ComponentProtocol:
        """Provide a component instance for testing.

        This abstract method must be implemented by subclasses to provide
        a properly configured component instance for testing.

        Args:
            *args: Variable positional arguments
            **kwargs: Variable keyword arguments

        Returns:
            A component that implements the ComponentProtocol

        """
        ...

    def test_flows_protocol(self, comp_fixture: ComponentProtocol) -> None:
        """Test that the component implements the ComponentProtocol.

        Args:
            comp_fixture: A component instance to test

        """
        assert isinstance(comp_fixture, ComponentProtocol)

    def test_comp_protocol_attrs(self, comp_fixture: ComponentProtocol) -> None:
        """Test that the component has the expected attributes and parameters.

        Verifies that the component's parameters match what's expected by
        the function parser.

        Args:
            comp_fixture: A component instance to test

        """
        fp = FunctionParser()
        comp_vars = fp.comp_vars(comp_fixture)  # type: ignore
        num_init_params = len(comp_fixture.__init__.__code__.co_varnames) - 1  # type: ignore
        func_params = fp.get_func_params(comp_vars)

        assert comp_vars if num_init_params > 0 else not comp_vars
        assert len(comp_vars) == num_init_params
        assert len(func_params) == num_init_params

    def test_comp_protocol_e2e(self, comp_fixture: ComponentProtocol) -> None:
        """Test end-to-end function creation for the component.

        Tests that a function can be successfully created from the component.

        Args:
            comp_fixture: A component instance to test

        """
        fp = FunctionParser()
        fp.create_function(comp_fixture)
