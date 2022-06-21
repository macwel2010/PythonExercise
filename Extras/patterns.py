num=int(input('enter the number : '))
for r in range(num,0,-1):
    print('#',end='')
    for j in range(r):
        print(' ',end='')
    print('#')