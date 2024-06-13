def amount_validation():

    while True:
        try:
            Amount = float(input("Enter the amount to be converted: "))
            
        except:
            print("the entered input is invalid")
            continue
        if Amount<0:
            print("Amount needs to greater than 0")
        else:
            break
     
    
amount_validation()