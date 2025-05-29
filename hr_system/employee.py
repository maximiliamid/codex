from dataclasses import dataclass

@dataclass
class Employee:
    """Represents an employee in the HR system."""

    id: int
    name: str
    base_salary: float
    allowances: float = 0.0
    marital_status: str = "S"  # S=single, M=married
    dependents: int = 0
