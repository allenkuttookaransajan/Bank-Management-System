import mysql.connector
from mysql.connector import errorcode
import Menu_accounts
import Menu_loans
import tkinter as tk

Lb1=''

def password(account_number,password_user):
    
    global Lb1
    
    window=tk.Tk()
    window.title('Menu')
    
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database="project")
        cur=con.cursor()
        query='select*from admin where adm_no='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            title=tk.Label(window,text="No matching account",font=('Arial',15))
            title.pack()
        else:
            for row in results:
                if row[2]==password_user:
                    title=tk.Label(window,text='Welcome to your account',font=('Arial',15))
                    title.pack()
                    
                    Lb1 =tk.Listbox(window,selectmode=tk.SINGLE)
                    Lb1.insert(1, "Add accounts")
                    Lb1.insert(2, "Delete account")
                    Lb1.insert(3, "Edit account")
                    Lb1.insert(4, "Display records")
                    Lb1.insert(5, "Search records")
                    Lb1.insert(6, "Transaction report")
                    Lb1.insert(7, "Save record")
                    Lb1.insert(8, "Display record on file")
                    Lb1.insert(9, "Add loan")
                    Lb1.insert(10,"Remove loan")
                    Lb1.insert(11,"Pay installments")

                    Lb1.pack()
                    
                    enter=tk.Button(window,text='Select',width=5,height=1,command=pass_menu)
                    enter.pack(side=tk.BOTTOM)
                    
                else:
                    title=tk.Label(window,text='Invalid password',font=('Arial',15))
                    title.pack()
                    
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('wrong datbase',err)
        else:
            print('some other error',err)
    
    window.mainloop()

def pass_menu():
    if Lb1.get(Lb1.curselection()) == 'Add accounts' or 'Delete account' or 'Edit account' or 'Display records' or 'Search records' or 'Transaction report' or 'Save record' or 'Display record on file':
        Menu_accounts.accounts_menu(Lb1.get(Lb1.curselection()))
    if Lb1.get(Lb1.curselection()):
        Menu_loans.loan_menu(Lb1.get(Lb1.curselection()))
        

    
    

            
    
                    
                          
            
    
