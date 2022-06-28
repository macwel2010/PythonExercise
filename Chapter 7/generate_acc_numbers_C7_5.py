import random

charge_acc = open(r"F:\Practice programms\Chapter 7\charge_acc_C7_5.txt", "w")
for i in range(365):
    s = str(random.randint(1000000, 9999999))
    charge_acc.write(f"{s}\n")
