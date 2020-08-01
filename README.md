# Group6_Assignment
Group 06 Assignment 2

$ git clone URL-of-Origin-Repo Directory-Address-of-Local-Repo

Project Description

This program seeks to help all users track their production hours in their companies.
It can also help employers also follow up on their employees by tracking the man hours that 
employees put in work. Hence makes it easy for employers to also monitor employees. 
This program was created by a DS_Group_6 team comprising of Benedict Nartey, Bernice Quarshie and 
Bright Kpatamasu. 

Goals
1. The user must be able to calculate the number of hours spent.
2. The user must be able to multiply the hours spent by the hourly pay to get the amount due him/her.


Algorithm
1. Needs to know who clocked in at a particular time.
2. Needs to know when the person clocked out.
3. Needs to know how many hours the person worked.
4. Need to convert the number of hours worked into money for pay.

1. To know who clocked in, type your name. Once you press enter, the time is recorded as your clock in time.
2. When you type in the same name and hit enter, it is recorded as your clock out time
3. The system calculates the difference in time as your hours spent working.
4. The hours spent working is multiplied by $5, which is the hourly pay to get your amount due you.

Number of working hours per day
daily pay = pay per hour * hours worked
Timestamp for reporting = date/time(24h) at the moment of clocking in
Timestamp for closing = date/time(24h) at the moment of clocking out.
hours worked per day = [date/time(24h) at the moment of clocking out - date/time(24h) at the moment of clocking in]
Total hours worked on task = sum of hours worked per day
Money made from working on task = Total hours worked on task * pay per hour

Dependencies
Datetime and CSV were imported.
