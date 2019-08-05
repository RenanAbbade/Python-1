import random

class Tank(object):

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__ (self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

        
    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")


def main():
    print("\n \n \n \n--------------- INICIO ---------------\n \n \n")
    #1)
    meuTanque1 = Tank("Bob")
    meuTanque2 = Tank("Renan")
    meuTanque3 = Tank("Leandro Pupo")
    meuTanque4 = Tank("Rafael Sanzio")
    meuTanque5 = Tank("Jean Marcos")

    Tanques = [meuTanque1, meuTanque2, meuTanque3, meuTanque4, meuTanque5]
    #2)a)

    while len(Tanques) > 1:
        tanqueAtaque = random.randint(0, len(Tanques)-1)
    
        #2)b)
        tanqueDano = random.randint(0 , len(Tanques)-1)

        while tanqueAtaque == tanqueDano:
            tanqueDano = random.randint(0 , len(Tanques)-1)

        print("----- ACTION ------- \n")
        Tanques[tanqueAtaque].fire_at(Tanques[tanqueDano])
        print("-------------------- \n")

        if Tanques[tanqueDano].alive == False:
            Tanques.pop(tanqueDano) 

        print("----- vivos -------- \n ")
        for i in range( 0,  len(Tanques), 1):
            print( Tanques[i] , "\n")
    for i in range( 0,  len(Tanques), 1):
            print("***vencedor**** \n ",Tanques[i])

main()