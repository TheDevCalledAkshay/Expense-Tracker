while True:
    print("NUM       OPTION")
    print("---       ------")
    print(" 1        Add Expense")
    print(" ")
    print(" 2        Add Income")
    print(" ")
    print(" 3        View Total Expense")
    print(" 4        View Total Income")
    print(" 5        View Balance")
    print(" ")
    print(" 6        EXIT")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        expense = int(input("Enter Expense: "))
        expense = str(expense)
        with open("expenses.txt",'a') as expenseFile:
            expenseFile.write(expense+'\n')
    elif choice == 2:
        income = int(input("Enter Income: "))
        income = str(income)
        with open("income.txt",'a') as incomeFile:
            incomeFile.write(income+'\n')
    elif choice == 3:
        with open("expenses.txt",'r') as readExpenseFile:
            reader = readExpenseFile.read()
            expenseList = reader.split('\n')
            duplicateList = []
            for i in expenseList:
                if i != '':
                    duplicateList.append(int(i)) 
            total = sum(duplicateList)
            print("TOTAL:",total)
    elif choice == 4:
        with open("income.txt",'r') as readIncomeFile:
            reader = readIncomeFile.read()            
            incomeList = reader.split('\n')
            duplicateList = []
            for i in incomeList:
                if i != '':
                    duplicateList.append(int(i)) 
            total = sum(duplicateList)
            print("TOTAL:",total)
    
    elif choice == 5:
        with open("expenses.txt",'r') as readExpenseFile:
            reader = readExpenseFile.read()
            expenseList = reader.split('\n')
            duplicateList = []
            for i in expenseList:
                if i != '':
                    duplicateList.append(int(i)) 
            total1 = sum(duplicateList)        
        with open("income.txt",'r') as readIncomeFile:
            reader = readIncomeFile.read()
            incomeList = reader.split('\n')
            duplicateList = []
            for i in incomeList:
                if i != '':
                    duplicateList.append(int(i)) 
            total2 = sum(duplicateList)
        balance = total2 - total1
        print("TOTAL BALANCE:", balance)

    elif choice == 6:
        break
    else:
        print("Please Choose A Valid Option")
