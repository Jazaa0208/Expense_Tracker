while True :
    print('''==============================
      Expense Tracker
==============================
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expense
5. Category-wise Expenses
6. Total Spending
7. Monthly Report
8. Exit
==============================''')
    choice = int(input("Enter your choice:"))
    file_path =r"D:\Ethans_Tech\Projects\Day 4\expense.txt"
    if choice == 1:
        while True :
            expense_name = input("Expense Name :")
            if expense_name =="":
                print("Expense Name cannot be Empty..!!")
            else :
                break
        while True :
            try:
                expense_Amount = float(input("Amount :"))
                if expense_Amount<=0:
                    print("Amount must be greater than 0.")
                else:
                    break
            except ValueError:
                print("Amount must be numeric.")
        while True :
            expense_Category = input("Category :")
            if expense_Category == "":
                print("Expense Category cannot be Empty..!!")
            else :
                break
        expense_Date = input("Date (DD-MM-YYYY):")
        with open(file_path,'r') as file:
            data = file.readlines()
        if len(data) == 0:
            with open(file_path,'a') as file:
                file.write("ID   Date         Name          Category         Amount\n")
                file.write("------------------------------------------------------------\n")
            index = 1
        else :
            for index, line in enumerate(data[2:], start=1):
                pass
            index += 1
        with open(file_path, "a") as file:
            file.write(
            f"{index:<5}"
            f"{expense_Date:<13}"
            f"{expense_name:<15}"
            f"{expense_Category:<17}"
            f"{expense_Amount:.2f}\n")

    if choice == 2:
        with open(file_path,'r') as file :
            data = file.readlines()
            expenses = data[2:]
            if len(expenses)== 0:
                print("No Expenses Recorded yet..!!")
            else :
                for line in data :
                    print(line ,end="")
    
    if choice == 3:
        print("-----------------------------------------")
        task_no = int(input("Enter Expense ID to Delete:"))
        print("-----------------------------------------")
        with open(file_path,'r') as file:
            tasks = file.readlines()

        tasks_actual =tasks[2:]
        if not tasks_actual:
            print("No Tasks Available..!!")
            continue  

        if task_no <= len(tasks_actual) and task_no>=1:
            tasks_actual.pop(task_no - 1)
            with open(file_path, 'w') as file:
                file.writelines(tasks[:2])
                for index, line in enumerate(tasks_actual, start=1):
                    parts = line.split()
                    file.write(
                    f"{index:<5}"
                    f"{parts[1]:<13}"
                    f"{parts[2]:<15}"
                    f"{parts[3]:<17}"
                    f"{parts[4]}\n")
            print("-----------------------------------------")
            print("Task Deleted Successfully!")
            print("-----------------------------------------")
        else :
            print("-----------------------------------------")
            print("Select the valid task Number ..!!")
            print("-----------------------------------------")
    
    if choice == 4:
        print("-----------------------------------------")
        search_category = input("Enter the Category : ")
        print("-----------------------------------------")

        with open (file_path,'r') as file :
            data = file.readlines()

        expenses = data[2:]

        if not expenses:
            print("-----------------------------------------")
            print("No Expenses Available..!!")
            print("-----------------------------------------")
        else :
            found = False

            print(data[0], end="")   # Header
            print(data[1], end="")   # Line

            for line in expenses:
                parts =line.split()

                if parts[3].lower() == search_category.lower():
                    print(line, end="")
                    found = True
                
            if not found :
                print("-----------------------------------------")
                print("No Expense Found in this Category.")
                print("-----------------------------------------")

    if choice == 5:
        print("-----------------------------------------")
        print("Category-wise Expense Report")
        print("-----------------------------------------")
        with open(file_path, 'r' ) as file :
            data = file.readlines()
        expenses = data[2:]
        if not expenses:
            print("-----------------------------------------")
            print("No Expenses Available..!!")
            print("-----------------------------------------")
        else :
            category_total ={}
            for line in expenses:
                parts = line.split()

                category = parts[3]
                amount = float(parts[4])

                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount
            
            for category, total in category_total.items():
                print("-----------------------------------------")
                print(category, "₹", total)
                print("-----------------------------------------")

    if choice == 6:
        print("-----------------------------------------")
        print("Total Expenses")
        print("-----------------------------------------")
        with open(file_path , 'r') as file :
            data = file.readlines()

        expenses = data[2:]
        if not expenses:
            print("-----------------------------------------")
            print("No Expenses Available..!!")
            print("-----------------------------------------")
        else :
            total = 0
            for line in expenses:
                parts = line.split()
                amount = float(parts[4])
                total +=amount
        print("-----------------------------------------")
        print(f"Total Expenses: {total:.2f}")
        print("-----------------------------------------")

    if choice == 7:
        print("-----------------------------------------")
        month_choice = input("Enter the Month :").lower()
        print("-----------------------------------------")
        months ={"january":1,
                 "feburary":2,
                 "march":3,
                 "april":4,
                 "may":5,
                 "june":6,
                 "july":7,
                 "august":8,
                 "september":9,
                 "october":10,
                 "november":11,
                 "december":12}
        value_choice = months[month_choice]
        
        with open(file_path,'r') as file :
            data = file.readlines()

            expenses=data[2:]
            if not expenses:
                print("-----------------------------------------")
                print("No Expenses Available..!!")
                print("-----------------------------------------")
            else:
                total =0
                for line in expenses:
                    parts=line.split()
                    date = parts[1].split("-")
                    if int(date[1])==value_choice:
                        total += float(parts[4])
                print("-----------------------------------------")
                print(f"Total Expenses in {month_choice.title()} {total}")
                print("-----------------------------------------")

    if choice == 8:
        print("-----------------------------------------")
        print("Thankyou for using Expense Tracker Application..!!")
        print("-----------------------------------------")
        break