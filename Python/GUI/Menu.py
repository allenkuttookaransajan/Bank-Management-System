import tkinter as tk
import Password_admin
import Password_account


window=tk.Tk()
window.title('Shinto Bank')

var1=tk.IntVar()
var2=tk.IntVar()

def enter0():
    global var1
    global var2
    
    title.configure(text='Are you an account holder or an employee')
    
    enter_0.destroy()
    
    var1=tk.IntVar()
    var2=tk.IntVar()
    C1 =tk.Checkbutton(window, text = "Employee",variable=var1,onvalue=1, offvalue=0,font=('Arial',12), height=5, width = 20)
    C2 =tk.Checkbutton(window, text = "Account holder",variable=var2,onvalue=1, offvalue=0,font=('Arial',12), height=5, width = 20)
    C1.deselect()
    C2.deselect()
    C1.pack()
    C2.pack()
    
    enter_1=tk.Button(window,text='select',width=5,height=1,command=enter1)
    enter_1.pack(side=tk.BOTTOM)
    
def enter1():
    
    global account_number
    global password_user
    global account_number1
    global password_user1
    
    for widget in window.winfo_children():
        widget.destroy()
    
    title1=tk.Label(window,text='Enter the required details',font=('Arial',15))
    title1.grid(column=2)
    
    if (var1.get()==1) and (var2.get()==0):    
        L1 =tk.Label(window, text="Employee number",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number=tk.Entry(window,bd=5)
        account_number.grid(column=3,row=1)

        L2=tk.Label(window,text='Password',font=('Arial',10))
        L2.grid(column=1,row=2)
        password_user=tk.Entry(window,bd=5)
        password_user.grid(column=3,row=2)
        
        enter_1=tk.Button(window,text='Enter',width=5,height=1,command=pass_admin)
        enter_1.grid(column=2,row=3)
        
            
    if (var1.get()==0) and (var2.get()==1):
        
        L1 =tk.Label(window, text="Account No",font=('Arial',10))
        L1.grid(column=1,row=1)
        account_number1=tk.Entry(window,bd=5)
        account_number1.grid(column=3,row=1)

        L2=tk.Label(window,text='Password',font=('Arial',10))
        L2.grid(column=1,row=2)
        password_user1=tk.Entry(window,bd=5)
        password_user1.grid(column=3,row=2)
        
        enter_1=tk.Button(window,text='Enter',width=5,height=1,command=pass_user)
        enter_1.grid(column=2,row=3)
        
def pass_admin():
    
    Password_admin.password(account_number.get(),password_user.get())
    
def pass_user():
    
    Password_account.password(account_number1.get(),password_user1.get())
    
title=tk.Label(window,text="Welcome to Shinto Bank",font=('Arial',15))
title.pack()

enter_0=tk.Button(window,text='Enter',width=5,height=1,command=enter0)
enter_0.pack(side=tk.BOTTOM)

window.mainloop()