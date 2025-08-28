 Expense Tracker

A Python-based desktop application to manage and analyze personal expenses with a clean and user-friendly GUI. Built using Tkinter for the interface, MySQL for database storage, and Matplotlib for expense visualization.


 Features:

  . Add Expenses with name, category, amount, and date

  . View All Expenses in a tabular format

  . Filter by Category & Date Range for better tracking

  . Visualize Spending with category-wise charts (Matplotlib)

  . Persistent Storage using MySQL database



 Tech Stack:

 . Python (Core logic & GUI with Tkinter)

 . MySQL (Database for storing expenses)

 . Matplotlib (Charts for visualization)



1. Install Required Packages:

pip install mysql-connector-python matplotlib


2. Database Setup:

CREATE DATABASE IF NOT EXISTS expense_tracker;
USE expense_tracker;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_name VARCHAR(100),
    category VARCHAR(50),
    amount DECIMAL(10,2),
    expense_date DATE
);




 






 
