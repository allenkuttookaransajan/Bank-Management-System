import mysql.connector
from mysql.connector import errorcode

def Deposit(account_number,balance):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='project')
        cur=con.cursor()
        query='select*from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            for row in results:
                query='update accountholder set balance=balance+'+str(balance)+' where (accountno='+str(account_number)+')'
                cur.execute(query)
                query2="insert into transaction values({},0,{},'Deposit',current_timestamp)".format(account_number,balance)
                cur.execute(query2)
                con.commit()
                print('##Deposited##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)
def Withdraw(account_number,balance):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='project')
        cur=con.cursor()
        query='select*from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            for row in results:
                query='update accountholder set balance=balance-'+str(balance)+' where (accountno='+str(account_number)+')'
                cur.execute(query)
                query2="insert into transaction values(0,{},{},'Withdraw',current_timestamp)".format(account_number,balance)
                cur.execute(query2)
                con.commit()
                print('##Withdrawn##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)
def Transfer(account_number,account_number_deposit,balance):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='project')
        cur=con.cursor()
        query='select*from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            for row in results:
                query1='update accountholder set balance=balance+'+str(balance)+' where (accountno='+str(account_number_deposit)+')'
                query2='update accountholder set balance=balance-'+str(balance)+' where (accountno='+str(account_number)+')'
                cur.execute(query1)
                cur.execute(query2)
                query3="insert into transaction values({},{},{},'Transfer',current_timestamp)".format(account_number,account_number_deposit,balance)
                cur.execute(query3)
                con.commit()
                print('##Deposited##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)
def Check_balance(account_number):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='Project')
        cur=con.cursor()
        query='select * from accountholder where accountno='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching record##')
        else:
            print('************************************************************************************************************')
            print('%15s'%"Account number",'%15s'%"Account name",'%10s'%"Balance",'%27s'%"E-mail",'%25s'%"Date of joining")
            print('************************************************************************************************************')
            for row in results:
                print('%15s'%row[0],'%15s'%row[1],'%10s'%row[2],'%27s'%row[3],'%25s'%row[4])
            print('************************************************************************************************************')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('some other error:',err)





    

    