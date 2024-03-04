import dataclasses


@dataclasses.dataclass(unsafe_hash=True)
class ComputeResources:
    cpu_cores: int = None
    ram_gb: int = None
    gpu_type: str = None
    gpu_count: int = 1
