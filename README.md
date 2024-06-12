# Employee Birthday Reminder System

##File Structure
1.Starting of with virtual environment --venv file
  Why a Virtual Environment?
  A virtual environment in Python is used to create an isolated environment for     Python projects. This isolation ensures that the dependencies and libraries        used by one project do not interfere with those used by another project
2.The second file is app file --app.py
   This controls this flow for files coming from the "controller folder"
   This is also the entry point .

3.The Controller Folder
  Inside the controller folder we have init__.py which imports all the files         present in the controller at once and send it to the app.py file
  
  Pls ignore the product controller file
  
  The "User_controller" file sends emails and as all the paths connecting it to       the user model file 
 4. The Model folder 
    Inside the model folder we have user_model which has all functions connected
    to the particular paths
  


This project is designed to send email reminders to managers about their employees' upcoming birthdays. The system sends reminders one week and one day before the employees' birthdays and updates the database accordingly.

## Table of Contents

- [Installation]
- [Configuration]
- [Usage]
- [Code Explanation]
- [Models]
- [Scheduler]

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Shnk22/EmployeeManagement.git
   cd EmployeeManagement
2. Set Up Virtual Environment
   python -m venv venv
   # On Windows, use `venv\Scripts\activate`
   # On Mac, use 'source venv/bin/activate'

3. The requirements for this are present in venv\Lib\site-packages

## Configuration
1. Ensure your MySQL database is set up and you have the necessary credentials. Update the database connection parameters in your script.
   db_connection = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

## Usage
 Run the Scheduler

The send_birthday_reminders function is scheduled to run at a specific interval using APScheduler. Ensure the scheduler is running to send out birthday reminders.

python
1. Run the Scheduler
The send_birthday_reminders function is scheduled to run at a specific interval using APScheduler. Ensure the scheduler is running to send out birthday reminders.

scheduler = BackgroundScheduler()
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

2.Trigger the Email Sending

  You can manually call the send_birthday_reminders function or set it up to run 
  at a specific interval as shown above.

## Code Explanation
1.Send_birthday_reminders Function
   This function retrieves employee data, checks if an employee's birthday is one    week or one day away, and sends email reminders to the respective managers. It     updates the EmailSentDateOneWeek or EmailSentDateOneDay fields in the 
    database once an email is sent.

 2.Update_email_sent_status Function
    This function updates the specified date field in the employee's record in         the database to indicate that an email has been sent.

3.Update_status_check Function
   This function updates the StatusCheck field to 'YES' after an email is sent.

4.reset_status_check Function
    This function resets the StatusCheck field to 'NO' one week after it was set 
     to 'YES'.
     
  ## Models
  
  Employee Model
  The employee model represents the structure of the employee data used in this     project. Below are the relevant fields:

  EmployeeID: Unique identifier for the employee.
  EmployeeName: Name of the employee.
  ManagerEmail: Email address of the employee's manager.
  EmployeeBirthDate: Birthdate of the employee.
  EmailSentDateOneWeek: Date when the one-week reminder email was sent.
  EmailSentDateOneDay: Date when the one-day reminder email was sent.
  StatusCheck: Indicates if the status check email has been sent (YES or NO).

Working on the Scheduler Part By using APS scheduler

This `README.md` file provides a comprehensive guide for setting up, configuring, and understanding the Employee Birthday Reminder System. Adjust the database connection details, repository URL, and any other specifics to match your project’s requirements.

   
