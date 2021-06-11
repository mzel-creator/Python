class Worker:
    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def getFullName(self):
        return f"{self.name} {self.surename}"

    def getFullProfit(self):
        return f"{sum(self._income.values())}"

manager = Position("Dorian", "Gray", "CEO", 500000, 125000)
print(manager.getFullName())
print(manager.position)
print(manager.getFullProfit())