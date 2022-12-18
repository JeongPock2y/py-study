class   Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result += x + y
        return self.result

cal = Calculator()
cal2 = Calculator()

#print(cal.add(1, 2))