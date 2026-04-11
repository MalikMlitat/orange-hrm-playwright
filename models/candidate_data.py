from dataclasses import dataclass


@dataclass
class CandidateData:
    first_name: str
    # middle_name: str = ""  # Optional
    last_name: str
    vacancy: str  # Default value, ensure this job exists in the system before running tests
    email: str
