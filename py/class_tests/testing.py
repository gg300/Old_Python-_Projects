class lol:
    def calc_price(self,x,y):
        return x*y

item=lol()
item.la= "item"
item.price = 42
item.quant = 3
print(item.calc_price(item.price,item.quant))

item1 = lol()
item1.la = "lol"
item1.price = 14
item1.quant = 5
print(item1.calc_price(item1.price,item1.quant))