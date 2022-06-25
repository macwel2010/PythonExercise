import random

steps = open(r"F:\Practice programms\Chapter 6\steps_C6_12.txt", "w")
for i in range(365):
    s = str(random.randint(1, 5000))
    steps.write(f"{s}\n")
