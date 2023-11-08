import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='First#1234',
    database='flask_tutorial'
)
            self.con.autocommit = True
            self.cur =self.con.cursor(dictionary=True)
            print("connection established")
        except:
            print("some error")
        # connection establishment code


    def user_getall_model(self):        
        # querry excecution code
        self.cur.execute("SELECT * from users")# self.con /self.cur is used to make the local variable global
        result=self.cur.fetchall()
        if len(result)>0:
            #return json.dumps(result)
            return make_response({"payload":result} ,200)
        else:
            return make_response({"message":"No Data found"},204)
        

    def user_addone_model(self , data):        
        # querry excecution code
        self.cur.execute(f"INSERT INTO users(name, email, phone, password, role) VALUES('{data['name']}' ,'{data['email']}' , '{data['phone']}' , '{data['password']}' , '{data['role']}')")# self.con /self.cur is used to make the local variable global
        #print(data) when to print all data
        #print(data['name'])
        return make_response({"message":"User created successfully"}, 200)
    

    def user_update_model(self , data):        
        # querry excecution code
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}',phone='{data['phone']}', password='{data['password']}', role='{data['role']}' WHERE id={data['id']}") # self.con /self.cur is used to make the local variable global
        #print(data) when to print all data
        #print(data['name'])
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"}, 201)
        else:
            return make_response({"message":"Nothing to update"}, 202)
    

    def user_delete_model(self , id):        
        # querry excecution code
        self.cur.execute(f"DELETE FROM users WHERE id={id}") # self.con /self.cur is used to make the local variable global
        #print(data) when to print all data
        #print(data['name'])
        if self.cur.rowcount>0:
            return make_response({"message":"User deleted successfully"}, 200)
        else:
            return make_response({"message":"Nothing to deleted"}, 202)
        

    def user_patch_model(self, data, id):
        qry ="UPDATE users SET "
        #print(data)
        for key in data:
            qry += f"{key}='{data[key]}',"
            
        qry = qry[:-1] + f" WHERE id={id}"    
        # UPDATE users SET col=val , vol=val WHERE id={id}

        self.cur.execute(qry) # self.con /self.cur is used to make the local variable global
        #print(data) when to print all data
        #print(data['name'])
        if self.cur.rowcount>0:
            return make_response({"message":"User updated successfully"}, 201)
        else:
            return make_response({"message":"Nothing to update"}, 202)

    def user_pagination_model(self, limit, page):
        limit = int(limit)
        page = int(page)
        start = (page*limit)-limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            res = make_response({"payload":result}, 200)
            return res
        else:
            return make_response({"message":"No Data found"}, 204)

    def user_upload_picture_model(self, uid, filepath):
        self.cur.execute(f"UPDATE users SET picture='{filepath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"File uploaded successfully"}, 201)
        else:
            return make_response({"message":"Nothing to update"}, 202)


    def user_login_model(self, data):
        return str(data)    