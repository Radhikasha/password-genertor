import random as r
import string as s
print("------------------- Greetings !! -----------------")
while 1:
    le=r.randint(8,12)
    u=s.ascii_uppercase
    l=s.ascii_lowercase
    d=s.digits
    sp=s.punctuation
    a=u+l+d+sp
    p=list(r.choice(u)+r.choice(l)+r.choice(d)+r.choice(sp)+''.join(r.choices(a,k=le-4)))
    r.shuffle(p)
    print()
    print('Your password is : ',*p,sep='')
    print()
    print("----------------------------------------------------")
    ch=input("Do you want to generate another password ( Yes or No ) : ").capitalize()
    if ch=="Yes":
        continue
    else:
        break