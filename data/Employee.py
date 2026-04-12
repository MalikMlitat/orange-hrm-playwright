from dataclasses import dataclass, field
from faker import Faker

faker = Faker()


@dataclass
class Employee:
    first: str = field(default_factory=faker.first_name)
    middle: str = field(default_factory=faker.first_name)
    last: str = field(default_factory=faker.last_name)
    emp_number: int = None
    pic_path: str = None

employee_1 = Employee()
employee_1.first
employee_1.last
employee_1.emp_number