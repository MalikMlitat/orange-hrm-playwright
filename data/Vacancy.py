from dataclasses import dataclass, field

from faker import Faker

faker = Faker()


@dataclass
class Vacancy:
    name: str = field(default_factory=faker.job)
    num_of_positions: int = 1
    description: str = field(default_factory=faker.sentence)
    status: bool = True
    is_published: bool = False
    job_title_id: int = None
    employee_id: int = None
    id: int = None
