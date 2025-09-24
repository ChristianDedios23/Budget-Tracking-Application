#when I add an expense I want the price, despriction, and if its a subscription, maybe replace subscription with a category
#give user ability to choose file name, import
import csv

expenses = []

def addExpense(date, category, price, description):
    expense = {
        "Date" : date,
        "Category" : category,
        "Price" : price,
        "Description" : description
    }
    expenses.append(expense)

def displayExpense():
    for item in expenses:
        for infoType in item:
            print(item[infoType])

def exportExpense():
    with open("output.csv", "w", newline="") as file:
        headerRow = ["Date", "Category", "Price", "Description"]
        writer = csv.DictWriter(file, fieldnames=headerRow)
        writer.writeheader()
        writer.writerows(expenses)
        
def importExpense(fileName):
    newExpense = []
    with open(fileName, mode="r", newline="") as file:
        csvReader = csv.DictReader(file)
        for row in csvReader:
            newExpense.append({
                "Date" : row["Date"],
                "Category" : row["Category"],
                "Price" : row["Price"],
                "Description" : row["Description"]
            })
        
        return newExpense
        



#addExpense("10-10-2008", "Food", 11.56, "Pizza")
#displayExpense()
expenses = importExpense("output.csv")
displayExpense()