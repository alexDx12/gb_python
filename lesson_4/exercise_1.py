from sys import argv

script_name, work_hours, work_rate, premium = argv
salary = int(work_hours) * int(work_rate) + int(premium)
print(work_hours)
print(work_rate)
print(premium)
print(salary)