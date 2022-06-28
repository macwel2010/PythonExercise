import random

charge_acc = open(r"F:\Practice programms\Chapter 7\USpopulation_C7_9.txt", "w")
for i in range(40):
    s = str(random.randint(1, 9))
    charge_acc.write(f"{s}\n")
