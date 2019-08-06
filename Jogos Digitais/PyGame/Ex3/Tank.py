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

    tanks = {} #Dicionario

    chaves = ["a","b","c","d","e","f", "g","h","i","j"] #lista de chaves

    chavesNovo = []

    quantidadeTanque = int(input("\nBem vindo ao jogo! \n"+
    "Quantos tanques deseja criar? "+
    "(minimo de 2, maximo de 10)\n"))

    while quantidadeTanque < 2  or quantidadeTanque > 10:

         quantidadeTanque = int(input("\nBem vindo ao jogo! \n"+
        "Quantos tanques deseja criar? "+
        "(minimo de 2, maximo de 10)\n"))
    
    for x in range(0,quantidadeTanque,1):

        print(" Jogador #",x+1)

        nome = str(input("Digite seu nome:\n" ))

        Tanque = Tank(nome)

        tanks[chaves[x]] = Tanque

        chavesNovo.append(chaves[x])

    tamanhoDic = len(tanks)

    print(tamanhoDic," jogadores cadastrados")
    
    while len(tanks) > 1:

        tanqueAtaque = random.choice(chavesNovo)

        print("tanque que irá atacar: ",tanks[tanqueAtaque])

        for chave in tanks:

            print("\n",chave,". Tanque:",tanks[chave])

        tanqueDano = str(input("\nDigite a letra que referencia o alvo na qual voce deseja atirar!  \n")).lower()
        
        while tanqueDano not in tanks or tanqueAtaque == tanqueDano:

             tanqueDano = str(input("\n ---- ATENCAO ----- \nEste indice não existe, ou voce não pode atacar a si mesmo! Por favor, escolha novamente! \n")).lower()

        print("\n tanque atacado: ", tanks[tanqueDano],"\n")

        tanks[tanqueAtaque].fire_at(tanks[tanqueDano])

        if tanks[tanqueDano].alive == False:
            tanks.pop(tanqueDano) 

        for chave in tanks:
            if tanks[chave].alive == False:
                tanks.pop(chave) 

            print("\n",chave,". Tanque:",tanks[chave])

        print("\n\n ---- Próxima rodada ---- \n")

   
    for chave in tanks:

        print("\n JOGADOR VENCEDOR: ",chave,". Tanque:",tanks[chave])


main()