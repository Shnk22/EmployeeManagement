import mysql.connector
import json
from datetime import date, datetime
class UserModel:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                password='yourdatabasePassword',
                user='root',
                database="databaseName"
            )
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection successful")
        except mysql.connector.Error as err:
            print(f"Some error: {err}")

   

    def user_birthday_model(self):
        self.cur.execute("SELECT EmployeeId,EmployeeName,ManagerEmail,EmployeeBirthDate,StatusCheck FROM employee WHERE MONTH(EmployeeBirthDate) = MONTH(CURDATE()) AND DAY(EmployeeBirthDate) BETWEEN DAY(CURDATE()) AND DAY(CURDATE()+7);")
        result = self.cur.fetchall()
        for row in result:
            for key, value in row.items():
                if isinstance(value, (date, datetime)):
                    row[key] = value.isoformat()
        
        if len(result) > 0:
            return {"payload":result}
        else:
            return {'message':'No data found'}

    def user_add_model(self,data):
        self.cur.execute(f"INSERT INTO employee (EmployeeId,EmployeeName,EmployeeBirthDate,EmployeeManager,ManagerEmail) VALUES ('{data['EmployeeId']}','{data['EmployeeName']}','{data['EmployeeBirthDate']}','{data['EmployeeManager']}','{data['ManagerEmail']}')")
        """ print(data["EmployeeId"]) """
        return {'message':"User Created Successfully "}
    
    def user_update_model(self,data):

        self.cur.execute(f"UPDATE employee SET StatusCheck = '{data['StatusCheck']}' WHERE EmployeeId = '{data['EmployeeId']}'")
        
        if self.cur.rowcount>0:
            return "User updated Successfully"
        else:
            return "Nothing to update"

    """ def user_delete_model(self,data):
        self.cur.execute(f"UPDATE employee SET EmployeeBirthDate = '{data['EmployeeBirthDate']}' WHERE EmployeeId = '{data['EmployeeId']}'")

        if self.cur.rowcount>0:
            return "User updated Successfully"
        else:
            return "Nothing to update" """
    def update_status_check(self,employee_id):
        print(employee_id)
        self.cur.execute(f"UPDATE employee SET StatusCheck = 'Yes' WHERE EmployeeId = '{employee_id}';")
    
