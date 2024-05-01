import dataclasses


@dataclasses.dataclass
class Resource:
    name: str = None
    id: str = None
    year: str = None
    color: str = None
    pantone_value: str = None
