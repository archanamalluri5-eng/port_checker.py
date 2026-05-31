Port Status Checker
 Project ID

task2

 Description

The Port Status Checker is a simple Python-based network tool that checks whether a specific port on a given host system is OPEN or CLOSED.

This project helps in understanding basic network communication, socket programming, and port scanning concepts in cybersecurity and system administration.

Features

Check if a port is open or closed
Works with both IP addresses and domain names
Input validation for port range (1–65535)
Handles errors like invalid host or input
Fast response using timeout
Simple command-line interface

Technologies Used

Python 3.x
Socket Programming (socket module)

 How to Run
 
1. Install Python

Make sure Python is installed:

python --version
2. Run the script
python port_checker.py

Input Example

Enter host (e.g., 127.0.0.1 or google.com): 127.0.0.1  
Enter port number: 80

 Output Example
[OPEN] Port 80 is OPEN on 127.0.0.1

or

[CLOSED] Port 8080 is CLOSED on 127.0.0.1
 Project Structure
Port-Status-Checker/
│
├── port_checker.py
└── README.md

Learning Outcomes:

Understanding TCP/IP ports
Basics of socket programming in Python
Error handling and input validation
Real-world networking concept implementation

Author

Archana


<img width="1281" height="760" alt="port_checker" src="https://github.com/user-attachments/assets/685acc8d-45b7-4c55-9f21-fcd85e69ccbd" />
