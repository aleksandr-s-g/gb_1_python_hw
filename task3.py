lines = []
try:
    with open("task3.txt", 'r') as f_obj:
        if not f_obj.readable():
            print("File is not readable")
            exit()
        lines = f_obj.readlines()
except:
    print("Some error with file!")

print(f"Num of lines:{len(lines)}")
salary_sum = 0
for i in range(0, len(lines)):
    salary = 0
    last_name = ''
    try:
        salary = float(lines[i].split(' ')[1])
        last_name = lines[i].split(' ')[0]
        salary_sum = salary_sum + salary
    except:
        print("wrong file format")
        exit()

    if salary < 20000:
        print(f"{last_name} {salary}")
print(f"avg_salary = {(salary_sum/len(lines)):.2f}")
