import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="root",port="3306" ,database="curd")
cursor=con.cursor()

cursor.execute("""create table users12(id int auto_increment primary key,
                                      user_name varchar(30),
                                    age int)""")


# create and insert the user db

def create_user(user_name,age):
    sql=("insert into users12(user_name,age)values(%s,%s)")
    values=(user_name,age)
    cursor.execute(sql,values)
    con.commit()
    print("insert sucessfully")



def read_user_data():
    sql=("select * from users12")
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in result:
        print(i)



def update_user(id,new_user_name,new_age):
    sql=("update users12 set user_name= %s,age= %s where id=%s")
    values=(id,new_user_name,new_age)
    cursor.execute(sql,values)
    con.commit()
    print("succesfully updated")



def delete_user1(id_user=1):
    sql=("delete from users12 where id=%s")
    value=(id_user,)
    cursor.execute(sql,value)
    con.commit()
    print("delete sucessfully")

create_user("praveen",30) 
read_user_data()  
update_user("maideen",100,1)
delete_user1()  

cursor.close()
con.close()
  



