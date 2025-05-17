# a=int(input("Введите первое число: "))
# b=int(input("Введите второе число: "))
# c=int(input("Введите третье число: "))
# nums = [a,b,c]
# nums. sort()
# print("Числа в порядке возрастания: ", nums[0],nums[1],nums[2])

# sales1=float(input("Введите уровень продаж первого менеджера: "))
# sales2=float(input("Введите уровень продаж второго менеджера: "))
# sales3=float(input("Введите уровень продаж третьего менеджера: "))
if sales1 <=500:
    salary1 =200+sales1*0.03
elif sales1 <= 1000:
    salary1 = 200 + sales1 * 0.05
else:
    sales1=200+sales1*0.08
if sales2 <=500:
    salary2 =200+sales2*0.03
elif sales2 <= 1000:
    salary2 = 200 + sales2 * 0.05
else:
    sales2=200+sales2*0.08
if sales3 <=500:
    salary3 =200+sales3*0.03
elif sales3 <= 1000:
    salary3 =200+sales3*0.05
else: sales3=200+sales3*0.08
best_salary=max(salary1,salary2,salary3)
if best_salary == salary1:
    salary1+200
    best =1
elif (best_salary == salary2):
    salary2 +=200
    best = 2
else:
    salary3 +=200
    best =3
    print(f"Зарплата 1 менеджера: {salary1} ")
    print(f"Зарплата 2 менеджера: {salary2} ")
    print(f"Зарплата 3 менеджера: {salary3} ")
    print(f"Лучший менеджер: {best} - ый ")


