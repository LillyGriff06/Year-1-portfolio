data1="--------------------------------------------"

def write():
    f=open("ESP practice.csv", "w")
    f.write(data1 + "\n")
    f.close()
write()

    
def productID():
    correct="False"
    while correct != "True":
        id = (input("Please enter the seven-digit product ID."))
        if len(id) != 7:
            print("You have not entered the correct ID.")
            correct="False"
        else:
            print("The ID you have entered is correct.")
            correct="True"
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The product ID is " + id + "\n")
        f.close()
    append()


def nameOfProduct():
    correct="False"
    while correct != "True":
        productName = input("Please enter the name of your product.")
        if len(productName) <= 0:
            print("You have not entered the correct product name.")
            correct="False"
        else:
            print("The product name entered is correct.")
            correct="True"
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The product name is " + productName + "\n")
        f.close()
    append()


def departmentName():
    correct="False"
    while correct != "True":
        productDep = input("Please enter the name of the product's department.")
        if len(productDep) <= 0:
            print("You have not entered the correct department name.")
            correct="False"
        else:
            print("The department name you have entered is correct.")
            correct="True"
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The product department name is " + productDep + "\n")
        f.close()
    append()


def productLocation():
    correct="False"
    while correct != "True":
        location = input("Please enter the location of the product as a letter then number.")
        if 1 < len(location) < 3:
            print("The location you have entered is correct.")
            correct="True"
        else:
            print("The location you have entered isn't correct.")
            correct="False"
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The product location is " + location + "\n")
        f.close()
    append()


def stockQuantity():
    totalStock = int(input("Please enter the quantity of stock you already have."))
    addStock = input("Are you adding stock? Answer y or n.")
    if addStock == "y":
        moreStock = int(input("Please enter how much stock you are adding."))
        totalStock = totalStock + moreStock
    elif addStock == "n":
        removeStock = input("Are you removing stock? Answer y or n.")
        if removeStock == "y":
            lessStock = int(input("Please enter how much stock you are removing"))
            totalStock = totalStock - lessStock
            if totalStock < 0:
                print("You don't have enough stock to remove that amount.")
                totalStock = 0
        elif removeStock == "n":
            print("The total amount of stock hasn't been changed")
        else:
            print("I don't understand what that means.")
    else:
        print("I don't understand what that means.")
    print("The total stock that has been tracked is ", totalStock, ".")
    totalStock=str(totalStock)
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The total stock is " + totalStock + "\n")
        f.close()
    append()


def priceEx():
    price = float(input("Please enter the price of the product."))
    vat = input("Does this price include VAT? Answer y or n.")
    if vat == "y":
        removeVAT = price/5
        price = price - removeVAT
    print("The price excluding VAT is £", price, ".")
    price=str(price)
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The price excluding VAT is £" + price + "\n")
        f.close()
    append()


def priceInc():
    price = float(input("Please enter the price of the product."))
    vat = input("Does this price include VAT? Answer y or n.")
    if vat == "n":
        addVAT = price/5
        price = price + addVAT
    print("The price including VAT is £", price, ".")
    price=str(price)
    def append():
        f=open("ESP practice.csv", "a")
        f.write("The price including the VAT is £" + price + "\n" + "--------------------------------------------" + "\n" + "\n" + "--------------------------------------------" + "\n")
        f.close()
    append()


repeat="True"
while repeat=="True":
    productID()
    nameOfProduct()
    departmentName()
    productLocation()
    stockQuantity()
    priceEx()
    priceInc()
    repeat=input("If you would like to continue to add products enter True.")
    
def read():
    f=open("ESP practice.csv", "r")
    f.close()
read() 
