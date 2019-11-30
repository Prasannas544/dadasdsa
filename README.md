# Assignment2020
# Entry Management System
This is a PyQt application serving the purpose of entry management software. There are five different options serving different purpose. First window giving all options then it redirect user to host check-in, visitor check-in, checkout and host info page. MySQL is used in back-end. This is having simple GUI with simple database having two tables. Functionality for email and sms can also be easily given by smtp library in python.




## Technology Stack

 1.  Python 3.7
 2.  PyQt5
 3.  MySQL
 4.  HTML, CSS

### Dependencies

1. MySqldb
2. QtSql
3.  time, datetime
4.  smtplib

## Assumptions
1.  Whenever host come he need to insert his data in (HOST CHECK IN) in order to recieve any visitor
2.  Everytime visitor also need to insert his details
3.  During check-in visitor need to tell his host
4.  Host list is available in fourth option


## How to Use
Download "Python Code" folder and run "python MAIN.py" in command prompt


# Workflow

#### Home Page
First page shows simply shows all the options.

![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/main.png)

#### Host Check In
If any new host want to register they can insert their details here, also successful insertion message is displayed here.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/HOST%20CHECKIN.png)

#### Visitor Check In
If any new visitor want to register they can insert their details here and the host name to whom they want to meet, if host is not present then error message is also displayed also for successful insertion host details are displayed.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/checkin%20(2).png)

#### Visitor Check Out
For check-out filling your details will insert your check-out time in the table automatically.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/checkout.png)

#### Host Available
List of all available host can be viewed.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/list.PNG)

#### Exit
To exit from the application.

## Database Schema
Build using Apache/2.4.41.
MySQL is used in back-end.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/table.png)

There are two tables:

### Visitor Table
Keeping all details in mind name, mobile number and host name are table as primary key.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/visitor.png)

### Host Table
Name is the only primary key.
![](https://github.com/Pragya007/Assignment2020/blob/master/Screenshots/host.png)


# Description
Must Read the "ENTRY MANAGEMENT SYSTEM.pdf" also Sql file of the database schema is there which can be easily imported to it.

# Author
Pragya  
(pragyachaurasia24@gmail.com)
