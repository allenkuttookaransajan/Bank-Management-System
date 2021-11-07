import Accounts
import tkinter as tk

account_number=''
account_name=''
account_balance=''
account_email=''
account_password=''
date=''
Lb1=''

def accounts_menu(ch):
    
    global account_number
    global account_name
    global account_balance
    global account_email
    global account_password
    global date
    global Lb1
    
    window=tk.Tk()
    window.title('Account')
    
    if ch=="Add accounts":
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)
            
        L2 =tk.Label(window, text="Name",font=('Arial',10))
        L2.grid(column=1,row=2)
        account_name=tk.Entry(window,bd=5)
        account_name.grid(column=3,row=2)
            
        L3 =tk.Label(window, text="Account balance",font=('Arial',10))
        L3.grid(column=1,row=3)
        account_balance=tk.Entry(window,bd=5)
        account_balance.grid(column=3,row=3)
            
        L4 =tk.Label(window, text="Email",font=('Arial',10))
        L4.grid(column=1,row=4)
        account_email=tk.Entry(window,bd=5)
        account_email.grid(column=3,row=4)
        
        L5 =tk.Label(window, text="Date of Joining",font=('Arial',10))
        L5.grid(column=1,row=5)
        date=tk.Entry(window,bd=5)
        date.grid(column=3,row=5)
            
        L6=tk.Label(window,text='Password',font=('Arial',10))
        L6.grid(column=1,row=6)
        account_password=tk.Entry(window,bd=5)
        account_password.grid(column=3,row=6)
            
        L6=tk.Label(window,text='Account type',font=('Arial',10))
        L6.grid(column=1,row=7)
            
        Lb1 =tk.Listbox(window,selectmode=tk.SINGLE)
        Lb1.insert(1, "Checking account")
        Lb1.insert(2, "Savings account")
        Lb1.insert(3, "Fixed deposit account")
        Lb1.insert(4, "Money market account")
        Lb1.insert(5, "Retirement account")

        Lb1.grid(column=3,row=7)
                    
        enter_1=tk.Button(window,text='Add',width=5,height=1,command=pass_add)
        enter_1.grid(column=2,row=8)

    elif ch=="Delete account":
        
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)
        
        enter_1=tk.Button(window,text='Delete',width=5,height=1,command=pass_delete)
        enter_1.grid(column=2,row=2)

    elif ch=="Edit account":
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)
            
        L2 =tk.Label(window, text="Balance",font=('Arial',10))
        L2.grid(column=1,row=2)
        account_balance=tk.Entry(window,bd=5)
        account_balance.grid(column=3,row=2)
        
        enter_1=tk.Button(window,text='Edit',width=5,height=1,command=pass_edit)
        enter_1.grid(column=2,row=3)

        
    elif ch=="Display records":
        Accounts.display_records_mysql()
        window.destroy()
    elif ch=="Search records":
        Accounts.search_records()
        window.destroy()
    elif ch=="Transaction report":
        Accounts.transaction_report()
        window.destroy()
    elif ch=="Save record":
        Accounts.save_all()
        window.destroy()
    elif ch=="Display record on file":
        Accounts.display_records_file()
        window.destroy()
    else:
        window.destroy()
            
def pass_add():
    
    Accounts.add_account(account_number.get(),account_name.get(),account_balance.get(),account_email.get(),date.get(),account_password.get(),Lb1.get(Lb1.curselection()))
 
def pass_delete():
    
    Accounts.delete_account(account_number.get())
    
def pass_edit():
    
    Accounts.edit_account(account_number.get(),account_balance.get())
    

            
            
