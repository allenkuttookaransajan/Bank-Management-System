import Loan
import tkinter as tk


def loan_menu(ch):
    
    global account_number
    global loaned_amount
    global interest
    global datewith
    global daterepay
    global Lb1
    global repayment
    
    window=tk.Tk()
    window.title('Loan')
    
    if ch=='Add loan':
        
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)
            
            
        L2 =tk.Label(window, text="Loaned amount",font=('Arial',10))
        L2.grid(column=1,row=2)
        loaned_amount=tk.Entry(window,bd=5)
        loaned_amount.grid(column=3,row=2)
            
        L3 =tk.Label(window, text="Interset",font=('Arial',10))
        L3.grid(column=1,row=3)
        interest=tk.Entry(window,bd=5)
        interest.grid(column=3,row=3)
        
        L4 =tk.Label(window, text="Date of withdrawal",font=('Arial',10))
        L4.grid(column=1,row=4)
        datewith=tk.Entry(window,bd=5)
        datewith.grid(column=3,row=4)
            
        L5=tk.Label(window,text='Date of repayment',font=('Arial',10))
        L5.grid(column=1,row=5)
        daterepay=tk.Entry(window,bd=5)
        daterepay.grid(column=3,row=5)
        
        L6=tk.Label(window,text='Loan type',font=('Arial',10))
        L6.grid(column=1,row=6)
            
        Lb1 =tk.Listbox(window,selectmode=tk.SINGLE)
        Lb1.insert(1, "Secured loan")
        Lb1.insert(2, "Student loan")
        Lb1.insert(3, "Home loan")
        Lb1.insert(4, "Payday loan")
        Lb1.insert(5, "Car loan")
        Lb1.insert(6, "Gold loan ")

        Lb1.grid(column=3,row=6)
                    
        enter_1=tk.Button(window,text='Add',width=5,height=1,command=pass_add)
        enter_1.grid(column=2,row=7)

        
    elif ch=='Remove loan':
        
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)
        
        enter_1=tk.Button(window,text='Delete',width=5,height=1,command=pass_delete)
        enter_1.grid(column=2,row=2)

        
    elif ch=='Pay installments':
        
        title=tk.Label(window,text='Enter the required details',font=('Arial',15))
        title.grid(column=2,row=0)
            
        L1 =tk.Label(window, text="Account number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)
        
        L2 =tk.Label(window, text="Ammount",font=('Arial',10))
        L2.grid(column=1,row=2)
        repayment=tk.Entry(window,bd=5)
        repayment.grid(column=3,row=2)
        
        enter_1=tk.Button(window,text='Pay',width=5,height=1,command=pass_repay)
        enter_1.grid(column=2,row=3)
    else:
        window.destroy()
        
        
def pass_add():
    
    Loan.add_loan(account_number.get(),Lb1.get(Lb1.curselection()),loaned_amount.get(),interest.get(),datewith.get(),daterepay.get())
    
def pass_delete():
    
    Loan.remove_loan(account_number.get())
        
def pass_repay():
    
    Loan.pay_insatllments(account_number.get(),repayment.get())
