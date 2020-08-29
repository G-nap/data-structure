print('*** multiplication or sum ***')
print('Enter num1 num2 : ',end='')
num1,num2 = [int(e) for e in input().split()]
if num1*num2>1000:
    print('The result is',num1+num2)
else:
    print('The result is',num1*num2)