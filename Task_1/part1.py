

text=input("Insert Comma separated binary numbers:")
try :
    numbers=text.split(',')
    divisibleby5=[]
    for ns in numbers:
        n=int(ns, base=2)

        if int(n%5)==0:
            divisibleby5.append(ns)
    print(','.join(divisibleby5))
except Exception as e:
    print(e)
        
