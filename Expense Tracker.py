import time

def loadingAnimation():
    for i in range(5):
        print(".", end = '')
        time.sleep(0.5)
    print(" ")

while True:
    print(" ")
    print("NUM       OPTION")
    print("---       ------")
    print(" 1        Add Expense")
    print(" 2        Reset Expense")
    print(" ")
    print(" 3        Add Income")
    print(" 4        Reset Income")
    print(" ")
    print(" 5        View Total Expense")
    print(" 6        View Total Income")
    print(" 7        View Balance")
    print(" ")
    print(" 8        EXIT")
    print(" ")

    choice = input("Enter Your Choice: ")
    print(" ")

    if choice == '1':
        expense = int(input("Enter Expense: "))
        expense = str(expense)
        with open("expenses.txt",'a') as expenseFile:
            expenseFile.write(expense+'\n')
    elif choice == '2':
        choiceContinue = input("Do You Want To Continue? Y/N: ")
        if choiceContinue in ['Y','y']:
            with open("expenses.txt",'w') as resetExpense:
                resetExpense.write('0')
                loadingAnimation()
                print("Expenses Have Been Reset")
    elif choice == '3':
        income = int(input("Enter Income: "))
        income = str(income)
        with open("income.txt",'a') as incomeFile:
            incomeFile.write(income+'\n')
    elif choice == '4':
        choiceContinue = input("Do You Want To Continue? Y/N: ")
        if choiceContinue in ['Y','y']:
            with open("income.txt",'w') as resetIncome:
                resetIncome.write('0')
                loadingAnimation()
                print("Income Has Been Reset")
    elif choice == '5':
        with open("expenses.txt",'r') as readExpenseFile:
            reader = readExpenseFile.read()
            print(reader)
            expenseList = reader.split('\n')
            duplicateList = []
            for i in expenseList:
                if i != '':
                    duplicateList.append(int(i)) 
            total = sum(duplicateList)
            print("TOTAL:",total)
    elif choice == '6':
        with open("income.txt",'r') as readIncomeFile:
            reader = readIncomeFile.read()
            print(reader)          
            incomeList = reader.split('\n')
            duplicateList = []
            for i in incomeList:
                if i != '':
                    duplicateList.append(int(i)) 
            total = sum(duplicateList)
            print("TOTAL:",total)
    
    elif choice == '7':
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

    elif choice == '8':
        print("Exiting Application")
        loadingAnimation()
        break
    else:
        print("Please Choose A Valid Option")