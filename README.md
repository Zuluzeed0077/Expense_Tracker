# Expense Tracker

### Goal

Build a terminal application that allows a user to record and analyze personal expenses.

### Core Features

- Add an expense
- Specify amount
- Specify category
- Add a description
- View all expenses
- Calculate total spending
- Calculate spending by category
- Delete an expense
- Save expenses to a file
- Load expenses when the program starts

### Example Data Model

```python
{
    "amount": 5000,
    "category": "Food",
    "description": "Lunch"
}
```

### Learning Objectives

#### Python Fundamentals
- Variables
- Strings
- Integers and floats
- Lists
- Dictionaries
- `if/else`
- `for` and `while` loops

#### Functions
- Creating functions
- Parameters
- Return values
- Breaking a program into smaller functions

#### Data Structures
Learn how dictionaries and lists can represent real-world information.

#### File Handling
- Reading files
- Writing files
- Saving application data
- Loading application data

#### Problem Solving
Learn to answer questions such as:
- How should an expense be represented?
- How should totals be calculated?
- How can expenses be grouped by category?

### Stretch Goal

Store expenses as JSON instead of plain text and use Python's `json` 
module.

### New things learned

- IMPORT: this brings module/library in to the program
- JSON: pythons json is library use for storing and loading data
- WITH: used for automatic resources management
- OPEN():used for opening file
- APPEND(): used for adding item to the end of a list
- POP(): used to remove and return item on a list
- JSON.LOAD: used for reading json file and turns it into python data
- JSON.DUMP:it takes ptython data and saves it as json
- ENUMERATE: it gives items position and its value while looping
- VALUE-ERROR: an error caused by an inappropriate value