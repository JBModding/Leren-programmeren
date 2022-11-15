from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
p = 9
# Jouw python instructies zet je vanaf hier:
while p > 0:
    p = p - 1
    robotArm.grab()
    color = robotArm.scan()

    if color == "red":
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for p in range(p):
            robotArm.moveLeft()
        p = p + 1

    else:
        robotArm.drop()
        for k in range(1):
            robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()