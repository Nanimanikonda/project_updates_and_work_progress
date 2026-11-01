# Bank Account Management System

## Project Overview
A basic Python project that demonstrates Object-Oriented Programming (OOP) and exception handling through bank account operations such as checking balance, crediting money, and debiting money.

## How It Works
- **BankAccount class:** Defines account details and banking operations.
- **Constructor (`__init__`):** Initializes the account holder's name, account number, and balance.
- **`check_balance()`:** Returns the current balance.
- **`credit_ammount()`:** Adds money to the existing balance.
- **`debit_amount()`:** Validates the withdrawal amount, checks available balance, and deducts money when valid. Exceptions are handled using `try-except`.

## Key Python Keywords and Concepts

| Keyword / Concept | Definition |
|---|---|
| `class` | Defines a blueprint for creating objects. |
| `def` | Defines a function or method. |
| `self` | Refers to the current object instance. |
| `__init__()` | Initializes an object's attributes when it is created. |
| `if` / `elif` / `else` | Control program execution based on conditions. |
| `try` | Contains code that may raise exceptions. |
| `except` | Handles specified exceptions. |
| `raise` | Explicitly raises an exception. |
| `as` | Assigns the caught exception to a variable. |
| `return` | Sends a result back to the caller. |
| `ValueError` | Exception used when a value is inappropriate. |
| `TypeError` | Exception raised when an operation uses incompatible types. |

**OOP Concepts:** Classes, objects, instance attributes, and instance methods.

## Technologies
- Python 3
- No external libraries required.