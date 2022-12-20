file = open('input.txt','r')

# make a dictionary to map letters to numbers
alphabet = "abcdefghijklmnopqrstuvwxyz"
priority = {}
# for lowercase
i = 1
for letter in alphabet:
    priority[letter] = i
    i += 1 
# add uppercase as well
for letter in alphabet:
    priority[letter.upper()] = i
    i += 1

# print(d)

priorities_sum = 0

while True:
    # read next line
    items = file.readline()
    if not items: # if line is empty
        break
    n = len(items)
    first_comp = items[:n//2]
    second_comp = items[n//2:]
    # make a set for second component
    set_second_comp = set()
    for item in second_comp:
        set_second_comp.add(item)
    # check each item of first component whether it belongs to the set
    # if it does then break and add its priority to priorities sum
    for item in first_comp:
        if item in set_second_comp:
            priorities_sum += priority[item]
            break

print(priorities_sum)
