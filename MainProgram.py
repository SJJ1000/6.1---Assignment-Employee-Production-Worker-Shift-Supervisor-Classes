from EmployeeClasses import ProductionWorker, ShiftSupervisor

def run_production_worker_demo():
    print("=== Production Worker Demo ===")
    name = input("Enter employee name: ")
    emp_number = int(input("Enter employee number: "))
    shift_number = int(input("Enter shift number (1 = day, 2 = night): "))
    hourly_pay = float(input("Enter hourly pay rate: "))

    worker = ProductionWorker(name, emp_number, shift_number, hourly_pay)

    # Display values using accessors
    print("\nProduction Worker Information")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_emp_number()}")
    print(f"Shift: {worker.get_shift_number()}")
    print(f"Hourly Pay: ${worker.get_hourly_pay():.2f}\n")


def run_shift_supervisor_demo():
    print("=== Shift Supervisor Demo ===")
    name = input("Enter supervisor name: ")
    emp_number = int(input("Enter supervisor employee number: "))
    salary = float(input("Enter annual salary: "))
    bonus = float(input("Enter production bonus: "))

    supervisor = ShiftSupervisor(name, emp_number, salary, bonus)

    # Display values using accessors
    print("\nShift Supervisor Information")
    print(f"Name: {supervisor.get_name()}")
    print(f"Employee Number: {supervisor.get_emp_number()}")
    print(f"Annual Salary: ${supervisor.get_salary():,.2f}")
    print(f"Annual Bonus: ${supervisor.get_bonus():,.2f}\n")


def main():
    run_production_worker_demo()
    run_shift_supervisor_demo()


if __name__ == "__main__":
    main()
