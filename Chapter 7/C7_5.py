valid_accounts_file = open(r"F:\Practice programms\Chapter 7\charge_acc_C7_5.txt", "r")
valid_accounts_list = []
for i in valid_accounts_file:
    valid_accounts_list.append(i.rstrip())
print(valid_accounts_list)
account_number = str(input("Enter the account number : "))
if account_number in valid_accounts_list:
    print("the account number is valid.")
else:
    print("The account numbeer is not valid.")
