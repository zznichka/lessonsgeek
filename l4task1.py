from sys import argv
name, work_hour, h_pay, prem = argv
for_pay = int(work_hour) * int(h_pay) + int(prem)
print(for_pay)
