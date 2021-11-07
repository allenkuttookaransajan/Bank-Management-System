import Transactions
import tkinter as tk

def transaction_menu(ch,account_number):
    
    global acc
    global account_deposit
    global account_withdraw
    global account_transfer
    global account_transfer1
    
    window=tk.Tk()
    window.title('Transaction')
    
    acc=account_number
    
    if ch=='Deposit':
            
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Amount to deposit",font=('Arial',10))
        L1.grid(column=1,row=2)
        account_deposit=tk.Entry(window,bd=5)
        account_deposit.grid(column=3,row=2)
            
        enter_1=tk.Button(window,text='Deposit',width=8,height=1,command=pass_deposit)
        enter_1.grid(column=2,row=3)

            
    elif ch=='Withdraw':
            
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Amount to withdaw",font=('Arial',10))
        L1.grid(column=1,row=2)
        account_withdraw=tk.Entry(window,bd=5)
        account_withdraw.grid(column=3,row=2)
            
        enter_1=tk.Button(window,text='Withdraw',width=9,height=1,command=pass_withdraw)
        enter_1.grid(column=2,row=3)
            
    elif ch=='Transfer':
            
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number to transfer",font=('Arial',10))
        L1.grid(column=1,row=2)
        account_transfer=tk.Entry(window,bd=5)
        account_transfer.grid(column=3,row=2)
            
        L2 =tk.Label(window, text="Amount to transfer",font=('Arial',10))
        L2.grid(column=1,row=3)
        account_transfer1=tk.Entry(window,bd=5)
        account_transfer1.grid(column=3,row=3)
            
        enter_1=tk.Button(window,text='Transfer',width=9,height=1,command=pass_transfer)
        enter_1.grid(column=2,row=4)

    elif ch=='Check balance':
        Transactions.check_balance(account_number)
    else:
        window.destroy()
            
def pass_deposit():
    
    Transactions.Deposit(acc,account_deposit.get())
    
def pass_withdraw():
    
    Transactions.Withdraw(acc,account_withdraw.get())
    
def pass_transfer():
    
    Transactions.Transfer(acc,account_transfer.get(),account_transfer1.get())
    
    