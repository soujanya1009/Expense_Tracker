import tkinter as tk
from tkinter import ttk, messagebox
from db_connect import get_connection
from datetime import date
import matplotlib.pyplot as plt
# Add Expense
def add_expense():
    name = expense_name_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    exp_date = date_entry.get()

    if not name or not category or not amount or not exp_date:
        messagebox.showerror("Error", "All fields are required")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (expense_name, category, amount, expense_date) VALUES (%s,%s,%s,%s)",
                   (name, category, amount, exp_date))
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("Success", "Expense added successfully!")
    clear_fields()
    view_expenses()
# View Expenses
def view_expenses(filter_category=None, start_date=None, end_date=None):
    for row in tree.get_children():
        tree.delete(row)
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM expenses WHERE 1=1"
    params = []
    if filter_category:
        query += " AND category=%s"
        params.append(filter_category)
    if start_date and end_date:
        query += " AND expense_date BETWEEN %s AND %s"
        params.extend([start_date, end_date])
    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    cursor.close()
    conn.close()
# Clear Fields
def clear_fields():
    expense_name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    filter_category_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)
# Show Expense Summary Graph
def show_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    if not data:
        messagebox.showinfo("Info", "No expenses to show")
        return
    categories, amounts = zip(*data)
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Summary by Category")
    plt.show()
# Tkinter GUI
root = tk.Tk()
root.title("Enhanced Expense Tracker")
# Input Fields
tk.Label(root, text="Expense Name").grid(row=0, column=0)
tk.Label(root, text="Category").grid(row=1, column=0)
tk.Label(root, text="Amount").grid(row=2, column=0)
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=3, column=0)
expense_name_entry = tk.Entry(root)
category_entry = tk.Entry(root)
amount_entry = tk.Entry(root)
date_entry = tk.Entry(root)
expense_name_entry.grid(row=0, column=1)
category_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)
date_entry.grid(row=3, column=1)
tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0, columnspan=2, pady=5)
# Filter Section
tk.Label(root, text="Filter by Category").grid(row=5, column=0)
filter_category_entry = tk.Entry(root)
filter_category_entry.grid(row=5, column=1)
tk.Label(root, text="Start Date (YYYY-MM-DD)").grid(row=6, column=0)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=6, column=1)
tk.Label(root, text="End Date (YYYY-MM-DD)").grid(row=7, column=0)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=7, column=1)
tk.Button(root, text="Apply Filter", 
          command=lambda: view_expenses(filter_category_entry.get(), start_date_entry.get(), end_date_entry.get())).grid(row=8, column=0, columnspan=2, pady=5)
tk.Button(root, text="Show Summary Graph", command=show_summary).grid(row=9, column=0, columnspan=2, pady=5)
# Treeview
columns = ("ID", "Expense", "Category", "Amount", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=10, column=0, columnspan=2)
view_expenses()
root.mainloop()
