import math
#Recursiva
def fat(n):
    if n == 0:
        return 1
    return n*fat(n-1)

#PRINCIPAL
print(fat(5))