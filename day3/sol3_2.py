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

    # read next three lines
    rucksack_1 = file.readline()

    # check if we have reached input end before proceeding
    if not rucksack_1:
        break

    rucksack_2 = file.readline()
    rucksack_3 = file.readline()

    # make sets for rucksacks 2 and 3
    set_rucksack_2 = set()
    for item in rucksack_2:
        set_rucksack_2.add(item)

    set_rucksack_3 = set()
    for item in rucksack_3:
        set_rucksack_3.add(item)

    # check each item of first rucksack whether it belongs to the second and third
    # if it does then break and add its priority to priorities sum
    for item in rucksack_1:
        if item in set_rucksack_2 and item in set_rucksack_3:
            priorities_sum += priority[item]
            break

print(priorities_sum)
