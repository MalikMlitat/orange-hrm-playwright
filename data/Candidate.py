from dataclasses import dataclass, field

from faker import Faker

faker = Faker()


@dataclass
class Candidate:
    first: str = field(default_factory=faker.first_name)
    middle: str = field(default_factory=faker.first_name)
    last: str = field(default_factory=faker.last_name)
    email: str = field(default_factory=faker.email)
    consent_to_keep_data: bool = True
    vacancy_id: int = None
    id: int = None
