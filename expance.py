#Expance Tracker Project

expenceList=[] #list of expanses in form of dictionary
print("Welcome to Expance Tracker :")

while True:
    print("====MENU====")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Expenses")
    print("4.Exit")

    choice=int(input("Please Enter Your Choice :"))

#ADD EXPENSE 
    if(choice==1):
        date=input("Enter the date :")
        category=input("what did you buy ? (food,bike,dresses,mobiles)  :")
        description=input("add more in detailed:")
        amount=float(input("Enter the amount:"))


        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenceList.append(expense)
        print("\n DONE bro .Expence added sucesfully")

#2.VIEW ALL EXPENSES

    elif(choice==2):
        if(len(expenceList)==0):
            print("NO expenses Added")
        else:
            print("=====These are total expense====")
            count=1
            for eachexpenditure in expenceList:
                print(f"expenditure number{count}  -> {eachexpenditure['date']} , {eachexpenditure['category']} , {eachexpenditure['description']} , {eachexpenditure['amount']} ")
                count=count+1

#3. view Total spending

    elif(choice==3):
        total=0
        for eachexpenditure in expenceList:
            total = total + eachexpenditure["amount"]

            print("\n TOTAL EXPENDITURE = ", total)

    #4.EXIT
    elif(choice==4):
        print("Thanks for using our MANI system")
        break
        
    else:
        print("INVALID CHOICE . TRY AGAIN")