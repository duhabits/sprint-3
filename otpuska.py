class Employee:
    vacation_days = 28
    remaining_vacation_days = vacation_days

    def __init__(self, first_name: str, second_name: str, gender: str):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

    def consume_vacation(self, mibus_days: int):
        self.remaining_vacation_days -= mibus_days

    def get_vacation_details(self):
        mes = f"Остаток отпускных дней: {self.remaining_vacation_days}."
        return mes


employee1 = Employee(first_name="aboba", second_name="qwe", gender="woman")
employee2 = Employee(first_name="qwe", second_name="QQWWEE", gender="man")

print(employee1)
employee1.consume_vacation(7)
print(employee1.get_vacation_details())
