import datetime
from db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(f'Текущая дата: {datetime.date.today()}')

