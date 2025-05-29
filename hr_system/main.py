from .employee import Employee
from .payroll import calculate_payroll


def main() -> None:
    """Run a simple payroll calculation for a sample employee."""
    employee = Employee(
        id=1,
        name="John Doe",
        base_salary=10_000_000,
        allowances=1_000_000,
        marital_status="S",
        dependents=0,
    )

    result = calculate_payroll(employee)

    print(f"Payroll for {employee.name}")
    print(f"Gross Salary   : Rp{result.gross_salary:,.2f}")
    print(f"BPJS Deduction : Rp{result.bpjs_deduction:,.2f}")
    print(f"Tax Deduction  : Rp{result.tax_deduction:,.2f}")
    print(f"Net Salary     : Rp{result.net_salary:,.2f}")


if __name__ == "__main__":
    main()
