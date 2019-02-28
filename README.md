# 4353FuelProject
Web application for ordering fuel from a fuel supplier. Created as a class project for COSC 4353.


# Requirements
Due Date: 03/01/2019 23:59:59

In this assignment you will build the front end for the web application that you designed in assignment 1. 
Remember, we are only building front end in this assignment.

Description: 
A partner of your company has requested to build a web application that will predict the
rate of the fuel based on the following criteria:
- Client Location
- Competitors rate
- Client rate history
- Gallons requested
- Company profit margin (%)
- Seasonal rate fluctuation (%)

Front end must include following components:
- Login (Allow Clientnt to register if not a client yet)
- Client Registration (Initially only username and Password)
- Client Profile Management (After client registers they should login first to complete the profile). Following fields will be on Profile page / form:
	- Full Name (50 characters, required)
	- Address 1 (100 characters, required)
	- Address 2 (100 characters, optional)
	- City (100 characters, required)
	- State (Drop Down, selection required) DB will store 2 character state code
	- Zipcode (9 characters, at least 5 character code required)
	
- Fuel Quote Form with following fields: (We are not building procing module yet)
	- Gallons Requested (numeric, required)
	- Delivery Address (Non-editable, comes from client profile)
	- Delivery Date (Calender, date picker)
	- Suggested Price (numeric non-editable, price will be calculated by Pricing Module - we are not building pricing module yet)
	- Total Amount Due (numeric non-editable, calculated (gallons * price))
	
- Fuel Quote History
	- Tabular display of all client quotes in the past. All fields from Fuel Quote are displayed.

- You should have validations in place for required fields, field types, and field lengths. 

Answer these questions:
NOTE: Only provide a word / pdf doc. Do not commit your code to SVN. University SVN has limitations on what type of file you can upload. You can use GIT for your group collaboration and code.

1.	Provide detailed sequence diagrams for major modules (login, profile, fuel quote, fuel history, pricing module)? (20)

2.	Discuss if your design and development methodolgy has changed since assignment 1 and why? (10)

3.	List what front end technologies you are using and why. List who is responsible of doing what in your group? (20)

3.	Provide screenshots of your front end, each page? (50)

What to turn in: 
- Only soft copy uploaded to SVN before due date. 
- No extensions.
- Frequently check in to SVN. 
- All group members must equally contribute.