text=input("Insert Comma separated binary numbers:")

numbers=text.split(',')

divisibleby5=[]

for ns in numbers:
    n=int(ns, base=2)'''Direct conversion to decimal from string'''

    if int(n%5)==0:'''checking divisibility condidion'''
        divisibleby5.append(ns)

print(','.join(divisibleby5))
        
        
