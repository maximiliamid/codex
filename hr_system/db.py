import json
from pathlib import Path
from typing import List

from .employee import Employee


class EmployeeDatabase:
    """Persist employee records in a JSON file."""

    def __init__(self, path: str = "employees.json") -> None:
        self.file_path = Path(path)
        self.employees: List[Employee] = []
        self.load()

    def load(self) -> None:
        """Load employees from the JSON file if it exists."""
        if self.file_path.exists():
            data = json.loads(self.file_path.read_text())
            self.employees = [Employee(**item) for item in data]
        else:
            self.employees = []

    def save(self) -> None:
        """Save current employees to the JSON file."""
        data = [e.__dict__ for e in self.employees]
        self.file_path.write_text(json.dumps(data, indent=2))

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        self.save()

    def list_employees(self) -> List[Employee]:
        return list(self.employees)
