from re import L
from alistirma import palindromik


palindromics=[str(x) for x in range(100,1000)]
index=0
for palindromic in palindromics:
    for i in palindromic[::-1]:
        palindromic+=i
    palindromics[index]=palindromic
    index+=1
bölenler = [ x for x in range(101,1000) if  x%10 ]
çapar=False
for x in palindromics[::-1]:
    for y in bölenler:
        if int(x)%y ==0 and int(x)/y<1000:
            print(x,y,int(x)/y)
            çapar=True
            break
    if çapar:
        break
