def menu():
  orders=[]
  print("-- STARBUCKS MENU--")
  print("1. Iced Coffee")
  print("2. Blonde Roast")
  print("3. Matcha Latte")
  print("4. Cold brew ")
  print("5. Caramel Macchiato ")
  print("6. Pumpkin Spice Latte")
  print("7. Peppermint Mocha")
  print("8. Iced Green Lemonade")
  print("9. Mango Dragonfruit")
  print("10. Iced Dirty Chai latte")
  option=input("What would you like to order? (1_10): ")
  while(option.lower()!="done"):
     if(option=='1'):
      orders.append("Iced Coffee")
     elif(option=='2'):
       orders.append("Blonde Roast")
     elif(option=='3'):
       orders.append("Matcha Latte")
     elif(option=='4'):
       orders.append("Cold brew ")
     elif(option=='5'):
       orders.append("Caramel Macc ")
     elif(option=='6'):
       orders.append("Pumpkin Spice Latte ")
     elif(option=='7'):
       orders.append("Peppermint Macha ")
     elif(option=='8'):
       orders.append("Iced Green ")
     elif(option=='9'):
       orders.append("Mango Dragonfruit")
     elif(option=='10'):
       orders.append("Iced Dirty Chai")
    
     option=input("Would you like anything else?: ") 
  print("Thank you for your order! Here is your order: ")
  for order in orders:
   print(order)
       
menu()