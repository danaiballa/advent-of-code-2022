file = open('input.txt','r')

pairs = 0

while True:

    # read next line
    assignment = file.readline()
    if not assignment: # if line is empty
        break

    # sections array will contain elf sections
    # for example if sections = [1, 5, 3, 8] then on input we had 1-5,3-8
    sections = []
    temp = ""

    for char in assignment:
        if char.isnumeric():
            temp += char
        elif char == "," or char == "-":
            sections.append(int(temp))
            temp = ""
    # add last one
    sections.append(int(temp))

    # check if assignment of second elf is contained in first
    if sections[0] <= sections[2] and sections[1] >= sections[3]:
        pairs += 1
    # check if assignment of first elf is contained in second
    elif sections[0] >= sections[2] and sections[1] <= sections[3]:
        pairs += 1
    
print(pairs)