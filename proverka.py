from main import Applicant

# три способа создать объект - все через один и тот же __init__
a1 = Applicant(1, "Иванов", "Иван", "Иванович", "Высшее", "Программист")
a2 = Applicant("2;Петров;Пётр;Петрович;Среднее;Слесарь;10 лет опыта")
a3 = Applicant('{"applicant_id":3,"last_name":"Сидоров","first_name":"Сидор","patronymic":"Сидорович","qualification":"Высшее","profession":"Юрист"}')

print(a1.last_name, a1.first_name)
print(a2.last_name, a2.profession)
print(a3.last_name, a3.qualification)