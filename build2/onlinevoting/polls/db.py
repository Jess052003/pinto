import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="voting"
    )
db =mydb.cursor()

def reg_user(name,address,phone,age,voters,uniid,password):
    sql="insert into voter(name,address,phone,age,voters,uniid,password) values(%s,%s,%s,%s,%s,%s,%s)"
    val=(name,address,phone,age,voters,uniid,password)
    db.execute(sql,val)
    if mydb.commit():
        return True
    return False

def verify(user,password):
    db.execute("select *from voter")
    res = db.fetchall()
    for x in res:
        if x[5]==user and x[6]==password:
            return True
        
    