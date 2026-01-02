import tkinter as tk
from tkinter import messagebox, ttk
import pymysql

def getConnection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1723@july",
        database="cusdb"
    )

def add_customer():
    con = getConnection()
    cur = con.cursor()

    qry = "INSERT INTO custb VALUES(%s,%s,%s,%s)"
    cur.execute(qry, (
        entry_id.get(),
        entry_name.get(),
        entry_age.get(),
        entry_mob.get()
    ))
    con.commit()
    con.close()
    messagebox.showinfo("Success","Customer Added")

def show_all():
    win = tk.Toplevel(root)
    win.title("All Customers")
    win.geometry("500x300")

    tree = ttk.Treeview(win, columns=("ID","Name","Age","Mobile"), show="headings")
    for col in ("ID","Name","Age","Mobile"):
        tree.heading(col,text=col)
        tree.column(col,width=100)
    tree.pack(fill=tk.BOTH,expand=True)

    con = getConnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM custb")
    for row in cur.fetchall():
        tree.insert("",tk.END,values=row)
    con.close()

def search_customer():
    con = getConnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM custb WHERE id=%s",(entry_id.get(),))
    data = cur.fetchone()
    con.close()

    if data:
        entry_name.delete(0,tk.END)
        entry_age.delete(0,tk.END)
        entry_mob.delete(0,tk.END)
        entry_name.insert(0,data[1])
        entry_age.insert(0,data[2])
        entry_mob.insert(0,data[3])
    else:
        messagebox.showerror("Error","Customer not found")

def delete_customer():
    con = getConnection()
    cur = con.cursor()
    cur.execute("DELETE FROM custb WHERE id=%s",(entry_id.get(),))
    con.commit()
    con.close()
    messagebox.showinfo("Deleted","Customer Deleted")

def update_customer():
    con = getConnection()
    cur = con.cursor()
    cur.execute("UPDATE custb SET name=%s, age=%s, mob=%s WHERE id=%s",
                (entry_name.get(),entry_age.get(),entry_mob.get(),entry_id.get()))
    con.commit()
    con.close()
    messagebox.showinfo("Updated","Customer Updated")

root = tk.Tk()
root.title("Tulsi's Customer Management System")
root.geometry("400x400")

labels = ["Customer ID","Name","Age","Mobile"]
for i,l in enumerate(labels):
    tk.Label(root,text=l).grid(row=i,column=0,pady=5)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_mob = tk.Entry(root)

entry_id.grid(row=0,column=1)
entry_name.grid(row=1,column=1)
entry_age.grid(row=2,column=1)
entry_mob.grid(row=3,column=1)

tk.Button(root,text="Add",width=15,command=add_customer).grid(row=5,column=0)
tk.Button(root,text="Search",width=15,command=search_customer).grid(row=5,column=1)
tk.Button(root,text="Update",width=15,command=update_customer).grid(row=6,column=0)
tk.Button(root,text="Delete",width=15,command=delete_customer).grid(row=6,column=1)
tk.Button(root,text="Show All",width=32,command=show_all).grid(row=7,column=0,columnspan=2,pady=5)

root.mainloop()
