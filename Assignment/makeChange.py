from _decimal import ROUND_HALF_UP
from _decimal import Decimal
def makeChange(amount=None): #function definition with optional variable to handle nothing input
    if amount!= None:
        if isinstance(amount, (int,float)): #check to make sure that input is a int or float
            amount = Decimal(str(amount)) #convert float or int to string and create decimal object to avoid rounding error
            if amount >= 0 and amount <= 100: #boundary conditions 0-100
                solution = [0,0,0,0,0,0,0,0]
                amount = Decimal(amount).quantize(Decimal('000.00'),ROUND_HALF_UP) #handling python3's desire to round like a banker
                while amount > 0:
                    if amount >= 20:
                        solution[0] += 1
                        amount -= Decimal(20)
                        continue
                    elif amount >= 10:
                        solution[1] += 1
                        amount -= Decimal(10)
                        continue
                    elif amount >= 5:
                        solution[2] += 1
                        amount -= Decimal(5)
                        continue
                    elif amount >= 1:
                        solution[3] += 1
                        amount -= Decimal(1)
                        continue
                    elif amount >= .25:
                        solution[4] += 1
                        amount -= Decimal(.25)
                        continue
                    elif amount >= .10:
                        solution[5] += 1
                        amount -= Decimal(.10)
                        continue
                    elif amount >= .05:
                        solution[6] += 1
                        amount -= Decimal(.05)
                        continue
                    else:
                        solution[7] += 1
                        amount -= Decimal(.01)
            else:
                solution = []
        else:
            solution = []
    else:
        solution = []
    return solution
        