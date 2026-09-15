from main import Applicant, ApplicantShort

full = Applicant(1, "Иванов", "Иван", "Иванович", "Высшее", "Программист", "+79991234567")
short = ApplicantShort(1, "Иванов", "Иван", "Иванович", "Программист", "+79991234567")

print(full)
print(short)