from datetime import datetime


name=input("Enter your name -->> ")
list  = '''
                1. SODA SOFT DRINKS                                     /50rs

                2. MILK                                                 /35rs

                3. CHIPS                                               /40rs       

                4. EGGS                                                 /6rs

                5. BREAD                                                /20rs

                6. BREAKFAST                                            /60rs

                7. CANDY BARS                                           /40rs

                8. BLOCK CHEES                                          /120rs

                9. BEER                                                 /200rs

                10. BOTTLED WATER                                       /25rs

                11. CIGARETTES                                          /50rs

                12. CHOCOLATE BARS                                      /130rs
              '''

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items

items={"SODA SOFT DRINKS":50,
       "milk":30,
       "chips":40,
       "eggs":6,
       "bread":20,
       "breakfast":60,
       "candy bar":40
       ,"block chees":120,
       "beer":200,
       "cigarette":50,
       "chocolate bar":130
       }

option=int(input("for list of items enter 1 -->>"))
if option==1:
  print(list)
  
for i in range(len(items)):
  inp1=int(input("if you want to bye enter 1 or exit press 2 -->>"))
  if inp1==2:
    break
  if inp1==1:
    item=input("enter your item -->>")
    quantity=int(input("enter your quantity -->>"))
    if item in items.keys():
      price=quantity*(items[item])
      pricelist.append((item,quantity,items,price))
      totalprice+=price
      ilist.append(item)
      qlist.append(quantity)
      plist.append(price)
      GST=(totalprice*5)/100
      finalamount=GST+totalprice
    else:
      print("you entered  item in not available**")
  else:
    print("you entered wrong number")
    
  inp=input("can i bill the items yes or no -->. ")
  if inp=='yes':
    pass
  if finalamount!=0:
    print(25*"=","**NKR SUPER MARKET***",25*"=")
    print(25*'-',"COIMBATORE",25*"-")
    print("name-->",name,30*" ","DATE TIME",datetime.now())
    print(75*"=")
    print("S NO",8*" ","items",8*" ",'quantity',8*" ",'price',8*" ")
    for i in range(len(pricelist)):
      print(i,12*" ",list[i],12*" ",qlist[i],12*" ",plist[i])
      print(75*"-")
      print(50*" ","GST",GST)
      print(50*" ",'totalamount',totalprice)
      print(75*"-")
      print(75*' ')
      print(25*'-',"THANKS FOR VISITING",25*'-')
      
      
    
      


