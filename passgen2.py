import random
print("Vitej v generatoru hesel.")

while True:
    r = input("Zadej delku hesla: ")
    if r.isdigit():
        print("V poradku vygeneruju",r,"znaku dlouhe heslo.")
        r = int(r)
        break
    else:
        print("Delka hesla musi byt cislo!")
        continue

while True:
    A = input('Musi obsahovat VELKE pismeno? 0-Nezalezi / 1-Ano ')
    if A == '0':
        A=0
        print('Nezalezi.')
        break
    elif A == '1':
        A=1
        print('Bude obsahovat Velke pismeno.')
        break
    else:
        print('Zadej 0 nebo 1 !')
        continue
while True:
    s = input('Musi obsahovat $pEci@lni znak? 0-Nezalezi / 1-Ano ')
    if s == '0':
        s=0
        print('Nezalezi.')
        break
    elif s == '1':
        s=1
        print('Bude obsahovat Velke pismeno.')
        break
    else:
        print('Zadej 0 nebo 1 !')
        continue
p=[]   
for i in range(r):
    p.append(random.randrange(0,4))
    if A == 1:
        for i in p:
            if i == '1':
                Ac = True
            else:
                Ac = False
    else:
        None
    if s == 1:
        for i in p:
            if i == '1':
                sc = True
            else:
                sc = False
                
if A == 1 and Ac == False:
    for i, n in enumerate(p):
        if n == 0:
            p[i] = 1

if s == 1 and sc == False:
    for i, n in enumerate(p):
        if n == 0:
            p[i] = 3
            
            
h=[]
for i in p:
    l=['*','/','@','!','#','$','%']
    if i == 0:
        h.append(chr(random.randrange(97,123)))
    elif i == 1:
        h.append(chr(random.randrange(65,91)))
    elif i == 2:
        h.append(chr(random.randrange(48,58)))
    else:
        h.append(chr(random.randrange(35,38)))
v=''
for i in h:
    v+=i
    
print(v)