import pandas as pd

data = pd.read_clipboard(header=None)[0].values

holder = set()

target = 2020

for num in data:
    needed = 2020 - num
    if needed in holder:
        print(needed, num)
        print(needed * num)
    holder.add(num)
