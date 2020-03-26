a = int(input('Key in a number: '))
b = int(input('Key in another number: '))
c = int(input('Key in another number: '))
if a > b > c:
    print(a,"is the greatest number.")
elif b > a > c:
    print(b,"is the greatest number.")
else:
    print(c,"is the greatest number.")
