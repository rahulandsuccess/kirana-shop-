class Mall:
    def __init__(self,items,people):
        self.items = items
        self.people = people

    def numberOfPeople(self):
        a = int(input('Enter the number of people entering:\n'))    
        if a > 10:
            print(f'{a} people cannot enter the mall')
            exit()

        else:
            print('welcome guys! Explore our luxury mall !')  

    def showItems(self):
        print('press 1 to show all the items')
        b = int(input('enter the number:\n'))
        if b == 1:
            print('Items in the mall are:\n',self.items)


    def buyItems(self):
        totalPriceOfAllTheItems = 0
        while(True):
            items = input('enter the items , you wanna buy ...')
            if items in self.items:
                print(f'how many {items}')
                quantity = int(input("enter the quantity:\n"))
                priceOfThatItem = quantity*500
                totalPriceOfAllTheItems += priceOfThatItem
                print(f'price is {priceOfThatItem}\n press')

            else:
                print(f'Sorry! {items} is not available in our mall.')   

            print('press 1 to continue or press 2 to exit')
            decision = int(input('enter your decision:\n'))
            if decision == 1:
                continue
            else:
                break
        print(f'total price of all the items are {totalPriceOfAllTheItems}')
        f = open('salary.txt','r')
        data = f.read()
        print(f'Your account has {data},press 1 to pay ') 
        pay = int(input('Enter the number:'))
        if pay == 1:
            if int(data)>totalPriceOfAllTheItems:
                data = int(data) - totalPriceOfAllTheItems
                print(f'you have paid the money\n now you have {data}')
                f = open('salary.txt','w')
                f.write(str(data))
            else:
                print('you donot have sufficient money!')       

# make an object
mall = Mall(['fish', 'potato', 'onion', 'cauliflower', 'aashirvaad aata', 'haathi tel'],10)
mall.numberOfPeople()
mall.showItems()
mall.buyItems()