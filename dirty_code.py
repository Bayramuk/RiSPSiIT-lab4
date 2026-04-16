import sys, math
import os

def CalculateDiscount(Price,Discount_percent):
    if Price<0 or Discount_percent<0:
       print("Ошибка")
       return 0
    FinalPrice=Price - (Price*(Discount_percent/100))
    return FinalPrice

class user_cart:
    def __init__( self , UserName ):
        self.UserName=UserName
        self.items = []
        
    def add_Item(self,item_price):
            self.items.append(item_price)

    def GET_TOTAL(self):
        s=0
        for i in self.items:
            s = s+i
        print( "Сумма без скидки: "+str(s) )
        # Здесь мы применяем скидку для вип клиентов которая составляет 15 процентов от общей суммы покупок в корзине пользователя
        return CalculateDiscount(s, 15)

C = user_cart("Иван")
C.add_Item(1000)
C.add_Item( 500 )
print("Итого со скидкой:",C.GET_TOTAL())