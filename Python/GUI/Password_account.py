import mysql.connector
from mysql.connector import errorcode
import Menu_transaction
import tkinter as tk

def password(account_number,password_user):
    
    global acc
    global Lb1
    
    acc=account_number
    
    window=tk.Tk()
    window.title('Transaction')
    
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database="project")
        cur=con.cursor()
        query='select*from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            for row in results:
                if row[6]==password_user:
                    title=tk.Label(window,text='Welcome to your account',font=('Arial',15))
                    title.pack()
                    
                    Lb1 =tk.Listbox(window,selectmode=tk.SINGLE)
                    Lb1.insert(1, "Deposit")
                    Lb1.insert(2, "Withdraw")
                    Lb1.insert(3, "Transfer")

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
            
def pass_menu():
    
    Menu_transaction.transaction_menu(Lb1.get(Lb1.curselection()),acc)
                    
                          
            
    