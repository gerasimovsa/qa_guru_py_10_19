import dataclasses


@dataclasses.dataclass
class User:
    email: str = None
    password: str = None
    first_name: str = None
    last_name: str = None
    id: str = None
    job: str = None
