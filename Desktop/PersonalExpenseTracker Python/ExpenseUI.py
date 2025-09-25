import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv

#Edits text in message box
def editEntryBox(string):
    messageBox.config(state="normal")
    messageBox.delete(0, tk.END)
    messageBox.insert(0, string)
    messageBox.config(state="disabled")

def deleteExpense():
    selectedItemID = treeView.selection()
    if(len(selectedItemID) > 0):
        for item in selectedItemID:
            treeView.delete(item)
        editEntryBox("Item was successfully deleted!")
    else:
        editEntryBox("No item to delete, please try again!")

def addExpense():
    if(len(dateEntry.get())  == 0):
        editEntryBox("Please enter a date!")
    
    elif(len(categoryEntry.get()) == 0):
        editEntryBox("Please enter a category!")
    
    elif(len(priceEntry.get()) == 0):
        editEntryBox("Please enter price!")
    
    elif(len(descriptionEntry.get()) == 0):
        editEntryBox("Please enter description!")
    
    else:
        editEntryBox("Item was successfully added!")
        treeView.insert("", tk.END, values=(dateEntry.get(), categoryEntry.get(),priceEntry.get(), descriptionEntry.get()))
        dateEntry.delete(0, tk.END)
        categoryEntry.delete(0, tk.END)
        priceEntry.delete(0, tk.END)
        descriptionEntry.delete(0, tk.END)

def exportExpense():
    filePath = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save CSV file as..."
    )

    if not filePath:
        return  # user canceled

    with open(os.path.basename(filePath), "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(treeView["columns"])
        
        for rowId in treeView.get_children():
            rowItems = treeView.item(rowId)["values"]
            writer.writerow(rowItems)
    
    editEntryBox("Table was successfully exported!")

def importExpense():
    filePath = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Open CSV file"
    )

    if not filePath:
        return #user canceled

    #not correct file
    if not filePath.lower().endswith(".csv"):
        editEntryBox("Error: Please select a CSV file only.")
        return

    with open(os.path.basename(filePath), mode="r", newline="") as file:
        csvReader = csv.reader(file)
        
        for rowID in treeView.get_children():
            treeView.delete(rowID)
        
        next(csvReader)

        for row in csvReader:
            treeView.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))
        
    editEntryBox("Table was successfully imported!")


#Initialize root frame
root = tk.Tk()
root.title("Expenses Tracker App")
root.geometry("600x400")
root.resizable(False,False)

#Allow for extension of the treeview in the grid
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)

#Left Frame
leftFrame = tk.Frame(root, width=150)
leftFrame.grid(row=0, column=0, sticky="n", padx=5, pady=5)

leftFrame.grid_columnconfigure(0, weight=1)
leftFrame.grid_columnconfigure(1, weight=1)
leftFrame.grid_rowconfigure(8, weight=1)


#Section 1 - Add labels and entrys

#Date Entry and Label
tk.Label(leftFrame, text="Date:").grid(row=0, column=0, padx=5, pady=5)
dateEntry = tk.Entry(leftFrame, width=15)
dateEntry.grid(row=0, column=1, padx=5, pady=5)

#Category Entry and Label
tk.Label(leftFrame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
categoryEntry = tk.Entry(leftFrame, width=15)
categoryEntry.grid(row=1, column=1)

#Price Entry and Label
tk.Label(leftFrame, text="Price:").grid(row=2, column=0, padx=5, pady=6)
priceEntry = tk.Entry(leftFrame, width=15)
priceEntry.grid(row=2, column=1)

#Description Entry and Label
tk.Label(leftFrame, text="Description:").grid(row=3, column=0, padx=5, pady=5)
descriptionEntry = tk.Entry(leftFrame, width=15)
descriptionEntry.grid(row=3, column=1)

#Section 2 - buttons
addButton = tk.Button(leftFrame, text="Add Expense", width=10, command=addExpense)
addButton.grid(row=4, column=0, pady=(5,0))

#Import button
importButton = tk.Button(leftFrame, text="Import CSV", width=9, command=importExpense)
importButton.grid(row=5, column=0, pady=(20,5))

#Export button
exportButton = tk.Button(leftFrame, text="Export CSV", width=9, command=exportExpense)
exportButton.grid(row=5,column=1, pady=(20,5))

#Delete button
deleteButton = tk.Button(leftFrame, text="Delete Expense", width=11, command=deleteExpense)
deleteButton.grid(row=6, column=0, pady=(15,0))

#Tells user to click expense first to delete it
tk.Label(leftFrame, text="Click Expense First").grid(row=7,column=0)

#Message box label, used to inform user of changes
tk.Label(leftFrame, text="Message Box:").grid(row=8, column=0, sticky="w", pady=(30,0))

#Message box
messageBox = tk.Entry(leftFrame)
messageBox.grid(row=9, column=0, columnspan=2, sticky="nsew", pady=(5,0))
messageBox.config(state="disabled")

#selectmode-can select one row at a time.
columnTags = ["Date", "Category", "Price", "Description"]
treeView = ttk.Treeview(root, selectmode="browse", show="headings", columns=columnTags)

for col in columnTags:
    treeView.heading(col, text=col)
    treeView.column(col, width=50)

#shows the tree
treeView.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

root.mainloop()