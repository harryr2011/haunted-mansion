import random
crit = random.randint(1, 3)
damage = random.randint(10, 20)
if (crit == 3):
    damage = damage * 2
    print("It was a critical hit")
    print("You took",damage,"damage")    
else:
    print("You took",damage,"damage")
