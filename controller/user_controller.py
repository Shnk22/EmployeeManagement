from app import app
from datetime import datetime,timedelta
from email.message import EmailMessage
from flask import jsonify
import ssl
import smtplib
from flask import request
from model.user_model import UserModel
obj=UserModel()

email_sender='xyz@gmail.com'
email_password='xyz'
def send_mail(email_reciever,subject,body):
    em=EmailMessage()
    em['From']= email_sender
    em['To']=email_reciever
    em['Subject']=subject
    em.set_content(body)

    """ SSL connection for making the line secure """
    context=ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_reciever,em.as_string())
            return {"status": "success"}
    except Exception as e:
        return {"status:'error','message'":str(e)}


""" User Birthdays """
@app.route('/user/birthdays')
def user_birthday():

    employees=obj.user_birthday_model()
    
    current_date = datetime.now().date()
    print(current_date)

    manager_dictOneWeek = {}
    manager_dictOneDay = {}
    for employee in employees['payload']:
        employee_id=employee['EmployeeId']
        employee_name = employee['EmployeeName']
        manager_email = employee['ManagerEmail']
        employee_birthday=datetime.strptime(employee['EmployeeBirthDate'],"%Y-%m-%d").date()
        one_week_before = employee_birthday - timedelta(days=7)
        one_day_before = employee_birthday - timedelta(days=1)
        statusCheck=employee['StatusCheck']

        if statusCheck=='NO':
            if one_week_before.month ==current_date.month and one_week_before.day == current_date.day:
                if manager_email in manager_dictOneWeek:
                    manager_dictOneWeek[manager_email].append((employee_name,employee_id))
                else:
                    manager_dictOneWeek[manager_email] = [(employee_name,employee_id)]
        
        if one_day_before.month == current_date.month and one_day_before.day == current_date.day:
            if manager_email in manager_dictOneDay:
                manager_dictOneDay[manager_email].append(employee_name)
            else:
                manager_dictOneDay[manager_email] = [employee_name]
    """ Sending mails """
    for manager_email, employee_details in manager_dictOneWeek.items():
        employee_names = ', '.join([name for name , _ in employee_details])
        subject = f"Upcoming Birthdays in a week: {employee_names}"
        body = "Dear Manager,\n\nThis is a reminder that the following employees have birthdays coming up this week:\n"
        for name , _ in employee_details:
            body += f"- {name} \n"
        body += "\nBest Regards,\nYour Company"
        
        email_status = send_mail(manager_email, subject, body)
       
        if email_status['status'] == 'success':
            for _ , employeeid in employee_details:
                obj.update_status_check(employeeid)



    
    for manager_email, employee_details in manager_dictOneDay.items():
        employee_names = ', '.join([name for name in employee_details])
        subject = f"Upcoming Birthdays tomorrow: {employee_names}"
        body = "Dear Manager,\n\nThis is a reminder that the following employees have birthdays coming up tomorrow:\n"
        for name , _ in employee_details:
            body += f"- {name} \n"
        body += "\nBest Regards,\nYour Company"

        email_status = send_mail(manager_email, subject, body)
    
    return jsonify({"status": "success"})

""" User Entries """ 
@app.route('/user/entries', methods=["POST"])
def user_entries(): 
    return obj.user_add_model(request. form)

@app.route('/user/update', methods=["PUT"])
def user_update(): 
    return obj.user_update_model(request. form)

@app.route('/user/delete', methods=["DELETE"])
def user_delete(): 
    return obj.user_update_model(request. form)
