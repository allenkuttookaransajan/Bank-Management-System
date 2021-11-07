import pickle
import mysql.connector
from mysql.connector import errorcode

def add_account(account_number,account_name,account_balance,email,date_of_joining,password,account_type):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database="project")
        cur=con.cursor()
        query="insert into accountholder values ({},'{}',{},'{}',{},'{}','{}')".format(account_number,account_name,account_balance,email,date_of_joining,account_type,password)
        cur.execute(query)
        con.commit()
        print("##Data saved##")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('wrong datbase',err)
        else:
            print('some other error',err)
            
def delete_account(account_number):
    
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='project')
        cur=con.cursor()
        query='select*from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('No matching results')
        else:
            query='delete from accountholder where accountno='+str(account_number)
            cur.execute(query)
            con.commit()
            print('##Record deleted##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)
            
def edit_account(account_number,balance):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='project')
        cur=con.cursor()
        query='select*from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            query='update accountholder set balance='+str(balance)+' where (accountno='+str(account_number)+')'
            cur.execute(query)
            con.commit()
            print('##Record edited##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)
def display_records_mysql():
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        query='select * from accountholder'
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No records to display##')
        else:
            count=0
            print('************************************************************************************************************')
            print('%15s'%"Account number",'%15s'%"Account name",'%10s'%"Balance",'%27s'%"E-mail",'%25s'%"Date of joining")
            print('************************************************************************************************************')
            for row in results:
                print('%15s'%row[0],'%15s'%row[1],'%10s'%row[2],'%27s'%row[3],'%25s'%row[4])
                count+=1
            print('*************************************** Total record:',count,'****************************************************')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('some other error:',err)
def search_records():
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        account_number=int(input('Enter account number to search: '))
        query='select * from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching record##')
        else:
            print('************************************************************************************************************')
            print('%15s'%"Account number",'%15s'%"Account name",'%11s'%"Balance",'%27s'%"Account Type",'%25s'%"Loan type")
            print('************************************************************************************************************')
            for row in results:
                print('%15s'%row[0],'%15s'%row[1],'%10s'%row[2],'%27s'%row[3],'%25s'%row[4])
            print('************************************************************************************************************')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('some other error:',err)

def transaction_report():
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        query='select * from Transaction'
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No records to display##')
        else:
            count=0
            print('************************************************************************************************************')
            print('%15s'%"Account withdrawn",'%19s'%"Account deposited",'%10s'%"Amount",'%27s'%"Transaction",'%16s'%"Time")
            print('************************************************************************************************************')
            for row in results:
                print('%15s'%row[0],'%15s'%row[1],'%15s'%row[2],'%27s'%row[3],'%25s'%row[4])
                count+=1
            print('*************************************** Total record:',count,'****************************************************')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('some other error:',err)
            
def save_all():
    f=open('Accounts.dat','wb')
    f1=open('Transaction.dat','wb')
    f2=open('Loan.dat','wb')
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        query='select * from Accountholder'
        cur.execute(query)
        results=cur.fetchall()
        acc=[]
        for row in results:
            acc=[row[0],row[1],row[2],row[3],row[4],row[5]]
            pickle.dump(acc,f)
    except EOFError:
        f.close()
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        query1='select * from Transaction'
        cur.execute(query1)
        results=cur.fetchall()
        tra=[]
        for row in results:
            tra=[row[0],row[1],row[2],row[3],row[4]]
            pickle.dump(tra,f1)
    except EOFError:
        f1.close()
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        query3='select * from Loan'
        cur.execute(query3)
        results=cur.fetchall()
        loan=[]
        for row in results:
            loan=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
            pickle.dump(loan,f2)
    except EOFError:
        f2.close()
    print('##Data Saved##')
    
def display_records_file():
    f1=open('Accounts.dat','rb')
    f2=open('Transaction.dat','rb')
    f3=open('Loan.dat','rb')
    print('************************************************************************************************************')
    print('%15s'%"Account number",'%15s'%"Account name",'%10s'%"Balance",'%20s'%"E-mail",'%25s'%"Date of joining",'%17s'%"Type of account")
    print('************************************************************************************************************')
    while True:
        try:
            row=pickle.load(f1)
            print('%15s'%row[0],'%15s'%row[1],'%10s'%row[2],'%27s'%row[3],'%18s'%row[4],'%15s'%row[5])
        except EOFError:
            f1.close()
            print('************************************************************************************************************')
            break
        except ValueError:
            f1.close()
            print('************************************************************************************************************')
            break
    print('************************************************************************************************************')
    print('%15s'%"Account withdrawn",'%20s'%"Account deposit",'%10s'%"Amount",'%27s'%"Transaction Type",'%20s'%"Time")
    print('************************************************************************************************************')
    while True:
        try:
            row=pickle.load(f2)
            print('%15s'%row[0],'%15s'%row[1],'%15s'%row[2],'%27s'%row[3],'%30s'%row[4])
        except EOFError:
            f2.close()
            print('************************************************************************************************************')
            break
        except ValueError:
            f2.close()
            print('************************************************************************************************************')
            break
    print('************************************************************************************************************')
    print('%15s'%"Account number",'%15s'%"Account name",'%10s'%"Loaned amount",'%27s'%"intreset",'%25s'%"Date of withdrawal",'%10s'%"Date of withdrawal")
    print('************************************************************************************************************')
    while True:
        try:
            row=pickle.load(f3)
            print('%15s'%row[0],'%15s'%row[1],'%10s'%row[2],'%27s'%row[3],'%25s'%row[4],'%10s'%row[5])
        except EOFError:
            f3.close()
            print('************************************************************************************************************')
            break
        except ValueError:
            f3.close()
            print('************************************************************************************************************')
            break




        

            
    
    
    
    




            
        

           