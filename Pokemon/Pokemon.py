class Pokemon:
    def __init__(self, new_name, new_weight, new_height,new_cp,new_food):
        self.__name = new_name
        self.__wight = new_weight
        self.__height = new_height
        self .__cp=new_cp
        self.__food=new_food

    def eat(self):
        print(f'eating{self.getfood()}')

    def make_noice(self):
        print('wow')
    def setname(self,n):
        self.__name=n;
    def setweight(self,n):
        self.__weight=n;
    def setheight(self,n):
        self.__height=n;
    def setcp(self,n):
        self.__cp=n;
    def setcp(self,n):
        return self.__cp;
    def setname(self,n):
        return self.__name;
    def setheight(self,n):
        return self.__height;
    def etweight(self,n):
        return self.__weight;
    def getfood(self):
        return self.__food;
class Pikachu(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_cp,new_food):
        super().__init__( new_name, new_weight, new_height, new_cp,new_food)

    def eat(self):
        print(f'pikaeatinaag{self.getfood()}')

    def make_noice(self):
        print('pikawosssw')

class jet(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_cp,new_food):
        super().__init__( new_name, new_weight, new_height, new_cp,new_food)

    def eat(self):
        print(f'jeteatinaag{self.getfood()}')

    def make_noice(self):
        print('getwosssw')

Pokemona=Pokemon('d','21212','3333','3333','e')

kipab=Pikachu('p','555','963',7,'q')
jeta=jet('n','88','99','9999','w')
ls=[Pokemona,jeta,kipab]

for item in ls:
    item.make_noice()
for item in ls:
    item.eat()