from dataclasses import dataclass

from .employee import Employee


@dataclass
class PayrollResult:
    gross_salary: float
    bpjs_deduction: float
    tax_deduction: float
    net_salary: float


def calculate_payroll(employee: Employee) -> PayrollResult:
    """Calculate a simple payroll for an employee."""
    # Gross salary consists of base salary plus allowances
    gross_salary = employee.base_salary + employee.allowances

    # Example BPJS deduction (placeholder rate: 4% of gross salary)
    bpjs_deduction = gross_salary * 0.04

    # Taxable income after BPJS
    taxable_income = gross_salary - bpjs_deduction

    # Simplified income tax calculation (placeholder: 5% of taxable income)
    tax_deduction = taxable_income * 0.05

    # Net salary after deductions
    net_salary = gross_salary - bpjs_deduction - tax_deduction

    return PayrollResult(
        gross_salary=gross_salary,
        bpjs_deduction=bpjs_deduction,
        tax_deduction=tax_deduction,
        net_salary=net_salary,
    )
