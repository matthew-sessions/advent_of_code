def ct(right=3, down=1):
    with open("input.txt", "r") as f:
        lines = f.readlines()
        rightt = 0
        t = 0
        for i in range(0, len(lines), down):
            line = lines[i].strip()
            l = len(line)
            if line[rightt] == "#":
                t += 1
            rightt = (right + rightt) % l
    return t


ct()
hold = None
for right, down in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    temp = ct(right, down)
    if not hold:
        hold = temp
    else:
        hold *= temp
print(hold)

