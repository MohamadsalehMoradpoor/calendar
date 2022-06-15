from calendar import month

with open("calendar.txt", "a") as f:
    for i in range(1, 13):
        f.write(month(2022, i))
        f.write("\n")