import random
print("Welcome to star restaurant :)")
name = input("Enter your name:")
while True:
      try:
           numb = int(input("Enter your phone number:"))
      except ValueError:
          print("please enter a valid number ")
          continue

      if numb<6000000000 :
         print("please enter a valid number")
      elif numb>9999999999:
         print("please enter a valid number")
         continue
      else:
         break
print(" ")
choice = 1
oc = 0
qty = 0
toto = 0
bill = ''
pb = ''
while choice>0:
  print("Press 1 for ordering starters:")
  print("Press 2 for ordering Main coarse:")
  print("Press 3 for ordering Deserts and Drinks:")
  print("Press 0 If Finished ordering:")
  print(" ")
  while True:
      try:
           choice = int(input("Enter your choice:"))
      except ValueError:
          print("please enter a valid choice from 0 to 3 ")
          continue

      if choice<0 :
         print("please enter a valid choice")
      elif choice>3:
         print("please enter a valid choice")
         continue
      else:
         break
  if choice==1:
    print("Press 1 for veg starters ")
    print("Press 2 for non veg starters ")
    print("Press 0 to go back:")
    print(" ")
    c1 = 1
    while c1>0:
     while True:
       try:
           c1 = int(input("Enter your choice:"))
       except ValueError:
           print("please enter a valid choice from 0 to 3 ")
           continue 

       if c1<0 :
         print("please enter a valid choice")
       elif c1>2:
         print("please enter a valid choice")
         continue
       else:
         break
     if c1==1:
       print("Item:                              price:")
       print("1)Paneer tikka                     ₹110")
       print("2)Veggie kebab                     ₹110")
       print("3)Paneer kebab                     ₹110")
       print("4)Spring roll                      ₹130")
       print("5)Gobi Manchurian                  ₹130")
       print("6)Smoked mushroom                  ₹130")
       print("7)Veg momos                        ₹130") 
       print("8)Corn Chana Chat                  ₹150")
       print("9)Vegetable cutlet                 ₹150")
       print("10)Veg lollipop                    ₹150")
       print("0 to go back to main menu")
       print(" ")
       vs = 1
       amt = 0
       t1 = 0
       while vs>0:
         while True:
           try:
               vs = int(input("Enter your choice by entering the number:"))
           except ValueError:
               print("please enter a valid choice from 0 to 10 ")
               continue
           if vs<0 :
             print("please enter a valid choice")
           elif vs>10:
             print("please enter a valid choice")
             continue
           else:
             break
         if vs==1:
           oc = 110
           bill ='Paneer tikka      '
         elif vs==2:
           oc = 110
           bill ='Veggie kebab      '   
         elif vs==3:
           oc = 110
           bill ='Paneer kebab      ' 
         elif vs==4:
          oc = 130
          bill = 'Spring roll       '
         elif vs==5:
          oc = 130
          bill = 'Gobi Manchurian   '
         elif vs==6:
          oc = 130
          bill = 'Smoked mushroom   '
         elif vs==7:
          oc = 130
          bill = 'Veg momos         '
         elif vs==8:
          oc = 150
          bill = 'Corn Chana Chat   '
         elif vs==9:
          oc = 150
          bill = 'Vegetable cutlet  '
         elif vs==10:
          oc = 150
          bill = 'Veg lollipop      '
         elif vs==0:
          break

         while True:
           try:
               qty = int(input("Enter the quantity :"))
               print(" ")
           except ValueError:
               print("please enter a valid choice ")
               continue
           if qty<0 :
              print("please enter a valid choice")
              continue
           else:
             break
         amt = oc*qty
         h = str(oc)
         i = str(qty)
         j = str(amt)
         t1 = t1+amt
         pb = pb+'\n'+bill+"   "+h+"    "+i+"    "+j
       print(" ")
       f = t1
       toto = f+toto
       if vs==0:
         break
       
     elif c1==2:
       print("Item:                              price:")
       print("1)Chicken tikka                    ₹160")
       print("2)Chicken chilli kebab             ₹160")
       print("3)Mutton kebab                     ₹160")
       print("4)Drums of Heaven                  ₹180")
       print("5)Garlic Chicken                   ₹180")
       print("6)Smoked Chicken                   ₹180")
       print("7)Chicken fried momos              ₹180") 
       print("8)Garlic Prawns                    ₹200")
       print("9)Mughlai Mutton                   ₹200")
       print("10)Apollo Fish                     ₹200")
       print("0 to go back to main menu")
       print(" ")
       nvs = 1
       amt2 = 0
       t2 = 0
       while nvs>0:
         while True:
           try:
               nvs = int(input("Enter your choice by entering the number:"))
           except ValueError:
               print("please enter a valid choice from 0 to 10 ")
               continue
           if nvs<0 :
              print("please enter a valid choice")
           elif nvs>10:
             print("please enter a valid choice")
             continue
           else:
             break
         if nvs==1:
           oc = 160
           bill = 'Chicken tikka     '
         elif nvs==2:
           oc = 160
           bill = 'Chicken kebab     '
         elif nvs==3:
           oc = 160
           bill = 'Mutton kebab      '
         elif nvs==4:
          oc = 180
          bill = 'Drums of Heaven   '
         elif nvs==5:
          oc = 180
          bill = 'Garlic Chicken    '
         elif nvs==6:
          oc = 180
          bill = 'Smoked Chicken    '
         elif nvs==7:
          oc = 180
          bill = 'Chicken fried momo'
         elif nvs==8:
          oc = 200
          bill = 'Garlic Prawns     '
         elif nvs==9:
          oc = 200
          bill = 'Mughlai Mutton    '
         elif nvs==10:
          oc = 200
          bill = 'Apollo Fish       '
         elif nvs==0:
          break

         while True:
           try:
               qty = int(input("Enter the quantity :"))
               print(" ")
           except ValueError:
               print("please enter a valid choice ")
               continue
           if qty<0 :
              print("please enter a valid choice")
              continue
           else:
             break
         amt2 = oc*qty
         h = str(oc)
         i = str(qty)
         j = str(amt2)
         t2 = t2+amt2
         pb = pb+'\n'+bill+"   "+h+"    "+i+"    "+j
       print(" ")
       f2 = t2
       toto = f2+toto
       if nvs==0:
         break
     elif c1==0:
       break
  elif choice==2:
     print("Press 1 for veg main course ")
     print("Press 2 for non veg main course ")
     print("Press 0 to go back:")
     print(" ")
     c2 = 1
     while True:
       try:
           c2 = int(input("Enter your choice:"))
       except ValueError:
           print("please enter a valid choice from 0 to 3 ")
           continue

       if c2<0 :
         print("please enter a valid choice")
       elif c2>2:
         print("please enter a valid choice")
         continue
       else:
         break
     while c2>0:
      if c2==1:
        print("Item:                              price:")
        print("1)Paneer fried rice                ₹150")
        print("2)Veg biryani                      ₹150")
        print("3)Paneer noodles                   ₹150")
        print("4)Veg fried rice                   ₹170")
        print("5)Mushroom noodles                 ₹170")
        print("6)mushroom rice                    ₹170")
        print("7)Veg hakka noodles                ₹190") 
        print("8)Kashmiri biryani                 ₹190")
        print("9)Schezwan noodles                 ₹190")
        print("10)Curd rice                       ₹100")
        print("0 to go back to main menu")
        print(" ")
        vm = 1
        amt3 = 0
        t3 = 0
        while vm>0:
          while True:
            try:
                vm = int(input("Enter your choice by entering the number:"))
            except ValueError:
                print("please enter a valid choice from 0 to 10 ")
                continue
            if vm<0 :
              print("please enter a valid choice")
            elif vm>10:
              print("please enter a valid choice")
              continue
            else:
              break
          if vm==1:
            oc = 150
            bill = 'Paneer fried rice '
          elif vm==2:
            oc = 150
            bill = 'Veg biryani       '
          elif vm==3:
            oc = 150
            bill = 'Paneer noodles    '
          elif vm==4:
           oc = 170
           bill = 'Veg fried rice    '
          elif vm==5:
           oc = 170
           bill = 'Mushroom noodles  '
          elif vm==6:
           oc = 170
           bill = 'Mushroom rice     '
          elif vm==7:
           oc = 170
           bill = 'Veg hakka noodles '
          elif vm==8:
           oc = 190
           bill = 'Kashmiri biryani  '
          elif vm==9:
           oc = 190
           bill = 'Schezwan noodles  '
          elif vm==10:
           oc = 100
           bill = 'Curd rice         '
          elif vm==0:
           break

          while True:
            try:
                qty = int(input("Enter the quantity :"))
                print(" ")
            except ValueError:
                print("please enter a valid choice ")
                continue
            if qty<0 :
               print("please enter a valid choice")
               continue
            else:
              break
          h = str(oc)
          i = str(qty)
          amt3 = oc*qty
          j = str(amt3)
          t3 = t3+amt3
          pb = pb+'\n'+bill+"   "+h+"    "+i+"    "+j
        print(" ")
        f3 = t3
        toto = f3+toto
        if vm==0:
          break
      elif c2==2:
        print("Item:                              price:")
        print("1)Chicken Noodles                  ₹180")
        print("2)Egg Noodles                      ₹180")
        print("3)Egg fried rice                   ₹180")
        print("4)Chicken Biryani                  ₹210")
        print("5)Lollipop Biryani                 ₹210")
        print("6)Spl Chicken Biryani              ₹220")
        print("7)Fish Biryani                     ₹240")
        print("8)Prawn Biryani                    ₹240") 
        print("9)Mutton Biryani                   ₹260")
        print("10)Kheema Biryani                  ₹280")
        print("0 to go back to main menu")
        print(" ")
        nvm = 1
        amt4 = 0
        t4 = 0
        while nvm>0:
          while True:
            try:
                nvm = int(input("Enter your choice by entering the number:"))
            except ValueError:
                print("please enter a valid choice from 0 to 10 ")
                continue
            if nvm<0 :
              print("please enter a valid choice")
            elif nvm>10:
              print("please enter a valid choice")
              continue
            else:
              break
          if nvm==1:
            oc = 180
            bill = 'Chicken Noodles   '
          elif nvm==2:
            oc = 180
            bill = 'Egg Noodles       '
          elif nvm==3:
            oc = 180
            bill = 'Egg fried rice    '
          elif nvm==4:
           oc = 210
           bill = 'Chicken Biryani   '
          elif nvm==5:
           oc = 210
           bill = 'Lollipop Biryani  '
          elif nvm==6:
           oc = 220
           bill = 'Spl Chick Biryani '
          elif nvm==7:
            oc = 240
            bill = 'Fish Biryani      '
          elif nvm==8:
            oc = 240
            bill = 'Prawn Biryani     '
          elif nvm==9:
            oc = 260
            bill = 'Mutton Biryani    '
          elif nvm==10:
            oc = 280
            bill = 'Kheema Biryani    '
          elif nvm==0:
           break

          while True:
            try:
                qty = int(input("Enter the quantity :"))
                print(" ")
            except ValueError:
                print("please enter a valid choice ")
                continue
            if qty<0 :
               print("please enter a valid choice")
               continue
            else:
              break
          amt4 = oc*qty
          h = str(oc)
          i = str(qty)
          j = str(amt4)
          t4 = t4+amt4
          pb = pb+'\n'+bill+"   "+h+"    "+i+"    "+j
        print(" ")
        f4 = t4
        toto = f4+toto
        if nvm==0:
          break
  elif choice==3:
    print("Press 1 for deserts ")
    print("Press 2 for drinks ")
    print("Press 0 to go back:")
    print(" ")
    c3 = 1
    while True:
       try:
           c3 = int(input("Enter your choice:"))
       except ValueError:
           print("please enter a valid choice from 0 to 3 ")
           continue

       if c3<0 :
         print("please enter a valid choice")
       elif c3>2:
         print("please enter a valid choice")
         continue
       else:
         break
    while c3>0:
      if c3==1:
       print("Item:                              price:")
       print("1)Vanilla ice cream                ₹100")
       print("2)Di-Choco ice cream               ₹100")
       print("3)Mango Ice cream                  ₹100")
       print("4)Red velvet cake                  ₹120")
       print("5)Choco lava cake                  ₹120")
       print("6)Special ice cream                ₹140")
       print("7)Mughal kheer                     ₹140")
       print("8)Apple pie                        ₹140") 
       print("9)Toffee pudding                   ₹160")
       print("10)Choclate sandae                 ₹160") 
       print("0 to go back to main menu")
       print(" ")
       d1 = 1
       amt5 = 0
       t5 = 0
       while d1>0:
         while True:
           try:
               d1 = int(input("Enter your choice by entering the number:"))
           except ValueError:
               print("please enter a valid choice from 0 to 10 ")
               continue
           if d1<0 :
             print("please enter a valid choice")
           elif d1>10:
             print("please enter a valid choice")
             continue
           else:
             break
         if d1==1:
           oc = 100
           bill = 'Vanilla ice cream '
         elif d1==2:
           oc = 100
           bill = 'Di-Choco ice cream'
         elif d1==3:
          oc = 100
          bill = 'Mango Ice cream   '
         elif d1==4:
          oc = 120
          bill = 'Red velvet cake   '
         elif d1==5:
          oc = 120
          bill = 'Choco lava cake   '
         elif d1==6:
          oc = 140
          bill = 'Special ice cream '
         elif d1==7:
          oc = 140
          bill = 'Mughal kheer      '
         elif d1==8:
          oc = 140
          bill = 'Apple pie         '
         elif d1==9:
           oc = 160
           bill = 'Toffee pudding    '
         elif d1==10:
           oc = 160
           bill = 'Chocolate sandae  '
         elif d1==0:
          break

         while True:
           try:
               qty = int(input("Enter the quantity :"))
               print(" ")
           except ValueError:
               print("please enter a valid choice ")
               continue
           if qty<0 :
              print("please enter a valid choice")
              continue
           else:
             break
         amt5 = oc*qty
         t5 = t5+amt5
         h = str(oc)
         i = str(qty)
         j = str(amt5)
         pb = pb+'\n'+bill+"   "+h+"    "+i+"    "+j
       print(" ")
       f5 = t5
       toto = f5+toto
       if d1==0:
         break
      elif c3==2:
        print("Item:                              price:")
        print("1)Sprite Mojito                    ₹100")
        print("2)Fantasy Fanta                    ₹100")
        print("3)Cocacola w/ice                   ₹100")
        print("4)peri-peri soda                   ₹100")
        print("5)Vanilla milkshake                ₹120")
        print("6)Choco milkshake                  ₹120")
        print("7)Berry milkshake                  ₹120")
        print("8)Tropical twist                   ₹150") 
        print("9)Kopi coffee                      ₹100")
        print("10)Iranian tea                     ₹100") 
        print("0 to go back to main menu")
        print(" ")
        d2 = 1
        amt6 = 0
        t6 = 0
        while d2>0:
          while True:
            try:
                d2 = int(input("Enter your choice by entering the number:"))
            except ValueError:
                print("please enter a valid choice from 0 to 10 ")
                continue
            if d2<0 :
              print("please enter a valid choice")
            elif d2>10:
              print("please enter a valid choice")
              continue
            else:
              break
          if d2==1:
            oc = 100
            bill = 'Sprite Mojito     '
          elif d2==2:
            oc = 100
            bill = 'Fantasy Fanta     '
          elif d2==3:
            oc = 100
            bill = 'Cocacola w/ice    '
          elif d2==4:
            oc = 100
            bill = 'peri-peri soda    '
          elif d2==5:
           oc = 120
           bill = 'Vanilla milkshake '
          elif d2==6:
           oc = 120
           bill = 'Choco milkshake   '
          elif d2==7:
           oc = 120
           bill = 'Berry milkshake   '
          elif d2==8:
           oc = 150
           bill = 'Tropical twist    '
          elif d2==9:
           oc = 100
           bill = 'Kopi coffee       '
          elif d2==10:
           oc = 100
           bill = 'Iranian tea       '
          elif d2==0:
           break

          while True:
            try:
                qty = int(input("Enter the quantity :"))
                print(" ")
            except ValueError:
                print("please enter a valid choice ")
                continue
            if qty<0 :
               print("please enter a valid choice")
               continue
            else:
              break
          amt6 = oc*qty
          h = str(oc)
          i = str(qty)
          j = str(amt6)
          t6 = t6+amt6
          pb = pb+'\n'+bill+"   "+h+"    "+i+"    "+j
        print(" ")
        f6 = t6
        toto = f6+toto
        if d2==0:
          break
  if choice==0:
    if toto>0:
       print(" ")
       print("Name:",name)
       print("Phone Number:",numb)
       print("")
       print("Food Name          price   qty   amount")
       print(pb)
       print("")
       print("Amount: ₹",toto)
       print('GST= ₹',round(18/100*toto,2))
       print('Service Tax= ₹',round(6/100*toto,2))
       print('VAT= ₹',round(14/100*toto,2))
       print('Total= ₹',round((18/100*toto)+(6/100*toto)+(14/100*toto)+toto,2))
       print("")
       print("Your token for food:",random.randrange(1,100))
       print("Do not forget to collect the bill")
       print("Thanks for visiting and make sure to visit us again")
       print("Feel free to send us your reviews at star.restaraunt@gmail.com")
    else:
      print("You didn't order anything :o")
 
