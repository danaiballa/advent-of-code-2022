file = open('input.txt','r')

max_calories = 0
cur_max = 0
sum_arr = []

while True:
    calories = file.readline()
    #print(calories)
    if not calories:
        break
    if calories == '\n':
        # print("cur max is: " + str(cur_max))
        if cur_max > max_calories:
            max_calories = cur_max
        sum_arr.append(cur_max)
        cur_max = 0
        # print("max calories is: " + str(max_calories))
    else:
        # print(calories)
        cur_max += int(calories)

sum_arr.sort(reverse = True)
print(sum(sum_arr[:3]))
#print(sum_arr[0])
#print(sum_arr[1])
#print(sum_arr[2])
# print(max_calories)



