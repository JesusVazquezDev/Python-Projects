#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:43:42 2022

@author: jesusvazquez
"""

# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message

# Function find_ID() takes two parameters, a student's name and a dictionary.
# Function find_ID() returns the ID associated with the student's name if the
# name is in the dictionary. Otherwise, the function throws a custom exception
# type, StudentInfoError, with the message "Student ID not found for studentName",
# where studentName is the name of the student.
def find_ID(name, info):
    # Type your code here.
    if(info.get(name) == None):
        raise StudentInfoError(f'Student ID not found for {name}')
    else:
        return info.get(name)
    
# Function find_name() takes two parameters, a student's ID and a dictionary. 
# Function find_name() returns the name associated with the student's ID if 
# the ID is in the dictionary. Otherwise, the function throws a custom exception
# type, StudentInfoError, with the message "Student name not found for studentID",
# where studentID is the ID of the student.
def find_name(ID, info):
    # Type your code here.
    for k,v in info.items():
        if(v == ID):
            return k
            
    raise StudentInfoError(f'Student name not found for {ID}')


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    userChoice = input()    # Read search option from user. 0: find_ID(), 1: find_name()
    
    # FIXME: find_ID() and find_name() may throw an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as excpt:
        print(excpt)
        exit()