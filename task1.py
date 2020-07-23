import sys
usage_msg = "usage :" + sys.argv[0] + " hours salary_per_hour award"
print(usage_msg)
try:
    hours = float(sys.argv[1])
    salary_per_hour = float(sys.argv[2])
    award = float(sys.argv[3])
except:
    print("Args error!", usage_msg)
    exit()

salary = hours * salary_per_hour + award

print (f"Salary: {salary}")





