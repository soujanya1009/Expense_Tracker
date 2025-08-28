
🔗**Expense Tracker**

 A Python-based desktop application to manage and analyze personal expenses with a clean and user-friendly GUI. Built using Tkinter for the interface, MySQL for database storage, and Matplotlib for expense         visualization  


 🔗**Features**

  . Add Expenses with name, category, amount, and date

  . View All Expenses in a tabular format

  . Filter by Category & Date Range for better tracking

  . Visualize Spending with category-wise charts (Matplotlib)

  . Persistent Storage using MySQL database



🔗**Tech Stack**

 . Python (Core logic & GUI with Tkinter)

 . MySQL (Database for storing expenses)

 . Matplotlib (Charts for visualization)


 ---


 1. Install Required Packages:

    pip install mysql-connector-python matplotlib


---

2. Database Setup:

   CREATE DATABASE expense_tracker;



   USE expense_tracker;

   CREATE TABLE expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        expense_name VARCHAR(100),
        category VARCHAR(50),
        amount DECIMAL(10,2),
        expense_date DATE
   );


---

1.Expense Entries

 
 <img width="1920" height="1080" alt="Screenshot 2025-08-28 194707" src="https://github.com/user-attachments/assets/f4ead26f-1eba-45f5-9cd2-a34b0af7c50d" />


---

2.Filter by Category


<img width="1920" height="1080" alt="Screenshot 2025-08-28 194748" src="https://github.com/user-attachments/assets/f23cfbcf-7369-4537-8f52-d2ac227133c2" />


---

3.Filter by Date Range


<img width="1920" height="1080" alt="Screenshot 2025-08-28 194912" src="https://github.com/user-attachments/assets/8a6f567d-b138-45b5-a6d9-7b312a0cc768" />


---

4.Expense Summary by Category


<img width="1920" height="1080" alt="Screenshot 2025-08-28 192634" src="https://github.com/user-attachments/assets/a5502e3f-92e2-43b9-8457-cfef017009cb" />



 
