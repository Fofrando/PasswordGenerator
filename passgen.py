import random
print("Vitej v generatoru hesel.")

while True:
    r = input("Zadej delku hesla nebo 'Q' pro ukonceni: ")
    if r.isdigit():
        print("V poradku vygeneruju",r,"znaku dlouhe heslo.")
        r = int(r)
        break
    elif r.lower() == 'q':
        print('Ukoncuji.')
        quit()

    else:
        print("Delka hesla musi byt cislo!")
        continue
h=[]
p=0
for i in range(r):
    l=['*','/','@','!','#','$','%']
    p=random.randrange(0,4)
    if p == 0:
        h.append(chr(random.randrange(97,123)))
    elif p == 1:
        h.append(chr(random.randrange(65,91)))
    elif p == 2:
        h.append(chr(random.randrange(48,58)))
    else:
        h.append(chr(random.randrange(35,38)))
v=''
for i in h:
    v+=i
    
print(v)