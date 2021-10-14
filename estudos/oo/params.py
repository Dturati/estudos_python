class Peoples:
    def __init__(self, people):
        self.people = people
    
    def __getitem__(self, item):
        return self.people[item]

class HauntedBus:
    def __init__(self, passengers: Peoples  = None):
        if passengers is None:
            self._passengers = []
        else:
            self._passengers =  (passengers)

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passenger(self, passenger):
            self._passengers.append(passenger)

    def remove(self,passenger):
        self._passengers.remove(passenger)
    
    def __getitem__(self, item):
        return self._passengers[item]

people = Peoples(["David","Jose", "Marinete"])
b1 = HauntedBus(people)
b1.passenger = "Joana"
print(b1[:])
print(people[:])

