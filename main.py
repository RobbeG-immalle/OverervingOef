import math
class Vorm:
    pass

class Cirkel(Vorm):
    def __init__(self, straal):
        self.straal = straal
    def omtrek(self):
        return self.straal * 2 * math.pi

    def oppervlakte(self):
        return self.straal * self.straal * math.pi
    
class Vierkant(Vorm):
    def __init__(self, zijde):
        self.zijde = zijde
    def omtrek(self):
        return self.zijde * 4
    def oppervlakte(self):
        return self.zijde * self.zijde

class Fiets:
    serienummer = 0

    def __init__(self, kleur):
        self.kleur = kleur

if __name__ == "__main__":
    
    c1 = Cirkel(2)
    c2 = Cirkel(4)

    v1 = Vierkant(4)
    v2 = Vierkant(8)
    
    values = [c1,c2,v1,v2]

    for v in values:
        print(f"De omtrek van het object is: {v.omtrek()} en de oppervlakte is: {v.oppervlakte()}")

    f = Fiets("Groen")
    print(f"Het serienummer van de fiets is: {f.serienummer} en de fiets is {f.kleur}")