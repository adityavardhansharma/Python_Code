import random
a = input('Enetr A Number: ' )
a = int(a)
r= random.randint(0,10)
if a == r:
    print("You Geussed It Correct\nThe Number Is ",a)
else:
    print("The Number Was:",r)
    print('\nBetter Luck Next Time')