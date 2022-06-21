tuition_fee=8000
print('Year\t\tFees')
print('____________________________________')
for i in range(1,6):  
    tuition_fee=tuition_fee+(0.03*tuition_fee)
    print(f'{i}\t\t{tuition_fee:.2f}')
