points = 0
strength = 5
intelegence = 5
health = 100
def statPoints():
    global points 
    global strength 
    global intelegence 
    global health 
    points = points + pointsGain
    print("You have",points,"stat poits to allocate between 3 stats")
    print("warning!! If you input an invalid choice you will lose all your stat points")
    print("strength-",strength,)
    print("intelegence-",strength,)
    print("health-",health,)
    while points > 0:
        print("you have unused stat points")
        print("how many points do you want to allocate to strength")
        strengthPoints = int(input("> "))
        if(strengthPoints > points):
            print("invalid choice")
            break
        points = points - strengthPoints
        strength = strength + strengthPoints
        if(points <= 0):
            break
        print("you have",points,"points remaining")
        print("how many points do you want to allocate to intelegence")
        intelegencePoints = int(input("> "))
        if(intelegencePoints > points):
            print("invalid choice")
            break
        points = points - intelegencePoints
        intelegence = intelegence + intelegencePoints
        if(points <= 0):
            break
        print("you have",points,"points remaining")
        print("how many points do you want to allocate to health")
        healthPoints = int(input("> "))
        if(healthPoints > points):
            print("invalid choice")
            break
        points = points - healthPoints
        healthPoints2 = healthPoints*10
        health = health + healthPoints2    
    print("Your stats are now")
    print("strength-",strength,)
    print("intelegence-",intelegence,)
    print("health-",health,)

pointsGain = 0
pointsGain = pointsGain + 20
statPoints()

