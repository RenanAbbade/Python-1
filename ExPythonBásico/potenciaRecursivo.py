import math
#Recursiva
def pot(base, exp):
    if exp == 0:
        return 1
    return base*pot(base,exp-1)

#PRINCIPAL
print(pot(3,3))