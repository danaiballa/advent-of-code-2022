file = open('input.txt','r')

choice_points = {"X" : 1, "Y": 2, "Z": 3}
equiv = {"X" : "A", "Y": "B", "Z": "C"}
wins = {"X": "C", "Y": "A", "Z": "B"}
points = 0

while True:
    choice = file.readline()
    if not choice:
        break
    opponent = choice[0]
    me = choice[2]
    points += choice_points[me]
    if equiv[me] == opponent:
        points += 3
    elif wins[me] == opponent:
        points += 6

print(points)
