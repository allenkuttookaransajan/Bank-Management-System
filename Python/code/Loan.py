import mysql.connector
from mysql.connector import errorcode

def add_loan(account_no,loan_type,loaned_amount,interest,date_of_withdrawal,date_of_repayment):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database="project")
        cur=con.cursor()
        query="insert into loan(Account_no,Loan_type,Loaned_amount,interest,Date_of_withdrawal,date_of_repayment,repayment_amount) values({},'{}',{},{},{},{},{})".format(account_no,loan_type,loaned_amount,interest,date_of_withdrawal,date_of_repayment,(int(loaned_amount)*(100+int(interest))//100))
        query1='update accountholder set balance=balance+'+str(loaned_amount)+' where (accountno='+str(account_no)+')'
        cur.execute(query)
        cur.execute(query1)
        con.commit()
        print('##Data saved##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('wrong datbase',err)
        else:
            print('some other error',err)
            
def remove_loan(account_number):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database="project")
        cur=con.cursor()
        query='select*from loan where account_no='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            query='delete from loan where Account_no='+str(account_number)
            for row in results:
                query1='update accountholder set balance=balance-'+str(row[6])+' where (accountno='+str(account_number)+')'
                cur.execute(query)
                cur.execute(query1)
                con.commit()
                print('##Record deleted##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)

def pay_insatllments(account_number,repayment):
    try:
        con=mysql.connector.connect(host='127.0.0.1',user='root',password='',database="project")
        cur=con.cursor()
        query='select*from loan where account_no='+str(account_number)
        cur.execute(query)
        results=cur.fetchall()
        if cur.rowcount<=0:
            print('##No matching results##')
        else:
            for row in results:
                query='update loan set repayment_amount=repayment_amount-'+str(repayment)+' where (account_no='+str(account_number)+')'
                query1='update accountholder set balance=balance-'+str(repayment)+' where (accountno='+str(account_number)+')'
                cur.execute(query)
                cur.execute(query1)
                con.commit()
                print('##Record updated##')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('Wrong database',err)
        else:
            print('Some other error',err)
     
    


        