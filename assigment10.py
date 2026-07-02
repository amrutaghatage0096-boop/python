class ShoppingCard():
    def __init__(self, Product_Name, Quantity, Price ):
        self.Product_Name = Product_Name
        self.Quantity = Quantity
        self.Price = Price
    def totalcost(self):
        total = self.Quantity * self.Price
        return total

    def displaybill(self):
        print("----------Shooping bill----------")
        print("Product_Name:", self.Product_Name)
        print("Quantity:", self.Quantity)
        print("Price:",self.Price)
        print("totalcost:", self.totalcost())

c = ShoppingCard("Thar", 6 , 1700000)
c.displaybill()    

