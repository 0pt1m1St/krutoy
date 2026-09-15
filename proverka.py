from main import Applicant, ApplicantShort

short = ApplicantShort(1, "Иванов", "Иван", "Иванович", "Программист", "+79991234567")
full = Applicant(1, "Иванов", "Иван", "Иванович", "Высшее", "Программист", "+79991234567")

print(short)                # __str__ базового класса -> short_info()
print(full)                 # __str__ Applicant -> full_info()
print(full.short_info())    # унаследованный метод, работает и для полного объекта
print(isinstance(full, ApplicantShort))  # True - Applicant это и есть ApplicantShort
print(full == Applicant(1, "Иванов", "Иван", "Иванович", "Высшее", "Программист", "+79991234567"))  # True