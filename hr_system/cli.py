import argparse
from .employee import Employee
from .payroll import calculate_payroll
from .db import EmployeeDatabase


def cmd_add(args: argparse.Namespace) -> None:
    db = EmployeeDatabase(args.db)
    employee = Employee(
        id=args.id,
        name=args.name,
        base_salary=args.salary,
        allowances=args.allowances,
        marital_status=args.marital,
        dependents=args.dependents,
    )
    db.add_employee(employee)
    print(f"Added employee {employee.name}")


def cmd_list(args: argparse.Namespace) -> None:
    db = EmployeeDatabase(args.db)
    for emp in db.list_employees():
        print(f"{emp.id}: {emp.name} - Rp{emp.base_salary:,.2f}")


def cmd_payroll(args: argparse.Namespace) -> None:
    db = EmployeeDatabase(args.db)
    for emp in db.list_employees():
        result = calculate_payroll(emp)
        print(f"Payroll for {emp.name}")
        print(f"  Gross Salary   : Rp{result.gross_salary:,.2f}")
        print(f"  BPJS Deduction : Rp{result.bpjs_deduction:,.2f}")
        print(f"  Tax Deduction  : Rp{result.tax_deduction:,.2f}")
        print(f"  Net Salary     : Rp{result.net_salary:,.2f}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="HR Management CLI")
    parser.add_argument("--db", default="employees.json", help="Path to employee database")
    subparsers = parser.add_subparsers(dest="command")

    add_p = subparsers.add_parser("add", help="Add a new employee")
    add_p.add_argument("id", type=int)
    add_p.add_argument("name")
    add_p.add_argument("salary", type=float)
    add_p.add_argument("allowances", type=float)
    add_p.add_argument("marital")
    add_p.add_argument("dependents", type=int)
    add_p.set_defaults(func=cmd_add)

    list_p = subparsers.add_parser("list", help="List employees")
    list_p.set_defaults(func=cmd_list)

    payroll_p = subparsers.add_parser("payroll", help="Process payroll for all employees")
    payroll_p.set_defaults(func=cmd_payroll)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
