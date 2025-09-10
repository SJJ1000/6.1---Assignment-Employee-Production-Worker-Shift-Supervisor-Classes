class Employee:
    def __init__(self, name: str, emp_number: int):
        self._name = name
        self._emp_number = emp_number

    # Accessors (getters)
    def get_name(self):
        return self._name

    def get_emp_number(self):
        return self._emp_number

    # Mutators (setters)
    def set_name(self, name: str):
        self._name = name

    def set_emp_number(self, emp_number: int):
        self._emp_number = emp_number


class ProductionWorker(Employee):
    def __init__(self, name: str, emp_number: int, shift_number: int, hourly_pay: float):
        super().__init__(name, emp_number)
        self._shift_number = shift_number
        self._hourly_pay = hourly_pay

    # Accessors
    def get_shift_number(self):
        return self._shift_number

    def get_hourly_pay(self):
        return self._hourly_pay

    # Mutators
    def set_shift_number(self, shift_number: int):
        self._shift_number = shift_number

    def set_hourly_pay(self, hourly_pay: float):
        self._hourly_pay = hourly_pay


class ShiftSupervisor(Employee):
    def __init__(self, name: str, emp_number: int, salary: float, bonus: float):
        super().__init__(name, emp_number)
        self._salary = salary
        self._bonus = bonus

    # Accessors
    def get_salary(self):
        return self._salary

    def get_bonus(self):
        return self._bonus

    # Mutators
    def set_salary(self, salary: float):
        self._salary = salary

    def set_bonus(self, bonus: float):
        self._bonus = bonus
