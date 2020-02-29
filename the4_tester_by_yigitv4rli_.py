import the4
import time
def flatten(lst):
    if len(lst) == 0:
        return []
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])

start_time = time.time()

wrong_count = 0
with open("the4_data.json","r") as file:
    lines = file.readlines()
    for i in range(len(lines)-1):
        lines[i] = lines[i][:-1]
    for line in lines:
        data = line.split(":::")
        data[0] = eval(data[0])
        data[1] = eval(data[1])
        for i in range(len(data[1])) :
            data[1][i].sort()
        result = the4.chalchiuhtlicue(data[0])
        for k in range(len(result)) :
            result[k].sort()
        # reslen  = len(flatten(result))
        # datlen = len(flatten(data[1]))
        # if reslen == datlen:
        if result == data[1]:
            print("Succesful")
        elif result != data[1]:
            print("Failed on {}".format(data[0]))
            print("Your work found: {}".format(result))
            print("It should have been {}.".format(data[1]))
            wrong_count += 1

            
            
end_time = time.time()

print("Execution time is: {}".format(end_time-start_time))
print("In {} cases, you've failed {} times.".format(len(lines),wrong_count))
