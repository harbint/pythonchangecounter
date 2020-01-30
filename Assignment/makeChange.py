from _pydecimal import Decimal
def makeChange(amount)  :
    if isinstance(amount, (int,float)):
        amount = Decimal(amount)
        if amount >= 0 and amount <= 100:
            solution = [0,0,0,0,0,0,0,0]
            amount = round(amount,2)
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
    return solution
        