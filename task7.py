import json
info = [{}, {}]

profit_sum = 0
plus_firm_count = 0
try:
    with open("task7.txt", 'r') as f_obj:
        if not f_obj.readable():
            print("File is not readable")
            exit()
        for line in f_obj:
            cur_firm = line.split(' ')
            profit = int(cur_firm[2]) - int(cur_firm[3])
            info[0][cur_firm[0]] = profit
            if profit >= 0:
                profit_sum = profit_sum + profit
                plus_firm_count = plus_firm_count + 1

except:
    print("Some error with file!")

info[1]['average_profit'] = round(profit_sum / plus_firm_count, 2)

try:
    with open("task7.json", 'w') as f_obj:
        if not f_obj.writable():
            print("File is not writable")
            exit()
        json.dump(info, f_obj)

except:
    print("Some error with file!")
