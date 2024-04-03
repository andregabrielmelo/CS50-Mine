from tabulate import tabulate
import pandas as pd

# Create an object to hold finance sheets together Spreadsheet

# Make a project about expenses, creating a object to make keeping your expenses easier
class FinanceSheet:
    columns = ["Date", "Category", "Expense", "Details"]
    
   # Objetc begins with an empty dict
    def __init__(self):
        self._table = {
            "Date": [],
            "Category": [],
            "Expense": [],
            "Details": [],
        }

    # A finance sheet prints a data frame. Sorted by, filter
    def __str__(self, sorted=None, filter=None):
        return str(pd.DataFrame(self.table))
    
    @property
    def table(self):
        return self._table
    
    # Add a line in the finance sheet, needing date, category, expense, and details are optional
    def add_expense(self, date, category, expense, details=None):
        self._table["Date"].append(date)
        self._table["Category"].append(category)
        self._table["Expense"].append(expense)
        self._table["Details"].append(details)

    # total expenses
    def total_expenses(self):
        return (sum(self.table["Expense"]))
    
    # Sum of all expenses from especific category
    def total_expenses_category(self, category):
        if not category:
            raise ValueError("Need a cetegory")
        
        sum = 0
        for item in self.table["Category"]:
            if item == category:
                sum = sum + self.table["Expense"][self.table["Category"].index(item)]
        
        return sum

    def modify_line(self, line, **kwargs):
        # Input validation
        if not isinstance(line, int):
            raise ValueError("Line must be an integer")
        if line < 0 or line >= len(self.table):
            raise IndexError("Line index out of range")

        # Modify line
        for key, value in kwargs.items():
            if key in FinanceSheet.columns:
                self.table[key][line] = value

        return True

    # Swap lines places
    def swap_lines(self, line1, line2):

        # Input validation
        if not isinstance(line1, int) or not isinstance(line2, int): # check if it's an integer
            raise ValueError("Line must be an integer")
        if (line1 < 0 or line2 < 0) or (line1 >= len(self.table) or line2 >= len(self.table)):
            raise ValueError("Line index out of range")
        
        # Make temp line. reading compreehension
        temp_line = {}
        for key in self.table:
            temp_line[key] = self.table[key][line1]

        # Swap line1 for line2
        for key in self.table:
            self.table[key][line1] = self.table[key][line2]

        # Line2 equals temp line
        for key, value in temp_line.items():
            self.table[key][line2] = value

        return True

    # delete line
    def delete_line(self, line):
        # Verify it's a valid line 
        if not isinstance(line, int):
            raise ValueError("Line must be an integer")
        if line < 0 or line >= len(self.table):
            raise ValueError("Line out of index")

        # Delete line
        for key in self.table:
            self.table[key].pop(line)

    
def main():
    January = FinanceSheet()
    print(January)
    January.add_expense(12, "electricity", 60)
    January.add_expense(18, "transportation", 100, "bus")
    print(January)
    print(f"Total January: {January.total_expenses()}")
    print(f"Total January transportation: {January.total_expenses_category('transportation')}")

    # Dict with things to modify
    modify = {
        "Expense": 70,
    }

    January.modify_line(line=0, **modify)
    print(January)

    January.swap_lines(0, 1)
    print(January)

    January.delete_line(1)
    print(January)

# Use this function to save the content in the tables in another file
def saveInSQL():
    ...

# total sum from the sum of all total expenses of the passed finance sheets
def function_2():
    ...

# Return data about a finance sheet. Fisrt date, last date, amount of expenses, total expense, highest expense, expense by category
def function_n():
    ...

# Monthly expenses


if __name__ == "__main__":
    main()