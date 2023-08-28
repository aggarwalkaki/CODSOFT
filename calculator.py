
print("CALCULATOR \n")

while True:
    print("choose a option\n 1.add \n 2.subtract\n 3.multiply \n 4.divide\n5.exit")
    options = int(input("enter your option  = "))
    if(options==5):
        print("exit from the calculator")
        break
    
    num1 = float(input("enter your first number = "))
    num2 = float(input("enter your second number = "))
    match options :
      case 1 :
        result = num1+num2
        print("your result is ",result)
        
      case 2 :
        result = num1-num2
        print("your result is ",result)
        
      case 3 :
        result = num1*num2
        print("your result is ",result)
        
      case 4 :
        result = num1/num2
        print("your result is ",result)
        
      case _ :
        print("INVALID CASE")
        