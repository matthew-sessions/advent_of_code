import pandas as pd

data = pd.read_clipboard(header=None).values

valid = 0
for rule, letter, pattern in data:

    min_ = int(rule.split("-")[0])
    max_ = int(rule.split("-")[1])
    letter = letter.split(":")[0]
    counter = 0
    for i in pattern:
        if i == letter:
            counter += 1
    if counter >= min_ and counter <= max_:
        valid += 1
print(valid)


### part two

valid = 0
for rule, letter, pattern in data:

    min_ = int(rule.split("-")[0]) - 1
    max_ = int(rule.split("-")[1]) - 1
    letter = letter.split(":")[0]

    if pattern[min_] == letter or pattern[max_] == letter:
        if pattern[min_] == letter and pattern[max_] == letter:
            continue
        valid += 1
print(valid)

