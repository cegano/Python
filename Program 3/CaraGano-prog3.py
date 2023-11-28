#Cara Gano- Program 3


def getTotal(price, quantity):
    
    total = price * quantity
    
    return total

   
def main():

    print("%5s %5s %5s %8s %5s" % ("Name", "Item", "Price", "Quantity", "Total"))
    f = open("makewaves.txt", "r")
    
    total = 0
   
    for record in f:
        name, item, price, quantity = record.strip().split(',')
        
        price = float(price)

        quantity = int(quantity)

        custTotal = getTotal(price, quantity)

        total += custTotal

        print("%-8s %-20s $%5.2f %3d $%6.2f" % (name, item, price, quantity, total))

    total = round(total, 2)
    print()
    print("The total for the whole day is " + str(total))

main()

        
        

    

      
