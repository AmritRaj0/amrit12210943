#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
School Timetable Generator

This program generates an optimal weekly timetable for a school based on 
classes, subjects, teachers, and period requirements.
"""

### DO NOT MODIFY THE CODE BELOW THIS LINE ###

# Define the input constraints
# Classes
classes = ["Class 6A", "Class 6B", "Class 7A", "Class 7B"]

# Subjects
subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Physical Education"]

# Weekly period requirements for each class and subject
# {class_name: {subject_name: number_of_periods_per_week}}
class_subject_periods = {
    "Class 6A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 6B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 7A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2},
    "Class 7B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2}
}
class_subject_check = {
    "Class 6A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 6B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 7A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2},
    "Class 7B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2}
}

# Teachers and their teaching capabilities
# {teacher_name: [list_of_subjects_they_can_teach]}
teachers = {
    "Mr. Kumar": ["Mathematics"],
    "Mrs. Sharma": ["Mathematics"],
    "Ms. Gupta": ["Science"],
    "Mr. Singh": ["Science", "Social Studies"],
    "Mrs. Patel": ["English"],
    "Mr. Joshi": ["English", "Social Studies"],
    "Mr. Malhotra": ["Computer Science"],
    "Mr. Chauhan": ["Physical Education"]
}

subject_faculty = {
    "Mathematics": ["Mrs. Sharma","Mr. Kumar"],
    "Science": ["Ms. Gupta","Mr. Singh"],
    "Social Studies": ["Mr. Singh","Mr. Joshi"],
    "English": ["Mrs. Patel","Mr. Joshi"],
    "Computer Science":["Mr. Malhotra"],
    "Physical Education": ["Mr. Chauhan"]
}
# School timing configuration
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6

### DO NOT MODIFY THE CODE ABOVE THIS LINE ###

classes = ["Class 6A","Class 6B","Class 7A","Class 7B"]
busy= {"Mr. Kumar": [],
    "Mrs. Sharma": [],
    "Ms. Gupta": [],
    "Mr. Singh": [],
    "Mrs. Patel": [],
    "Mr. Joshi": [],
    "Mr. Malhotra": [],
    "Mr. Chauhan": []
    }

def check_busy(teacher, day, time):
    for i in busy[teacher]:
        if(i[0]==day and i[1]==time):
            return true
    return false

def generate_timetable():
    """
    Generate a weekly timetable for the school based on the given constraints.
    
    Returns:
        dict: A data structure representing the complete timetable
              Format: {day: {period: {class: (subject, teacher)}}}
    """
    # Initialize an empty timetable
    timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
    
    for period in range(1,7):
        for day in range(1,8):
            for c in classes:
                flag=0
                for i in class_subject_check[c]:
                    if(class_subject_check[c][i]!=0):
                        for(k in class_subject_check[c]):
                            for faculty in subject_faculty[class_subject_check[c]]:
                                if(check_busy(faculty,day,period)()!=true):
                                    timetable[day[period]]={class_subject_check[c],faculty}
                                    print(timetable[day[period]])

                                    busy[faculty]=(day,period)
                                    flag=1
                                    break
                                class_subject_check[c][i]-=1
                                if(flag==1):
                                    break
                    



    # TODO: Implement the timetable generation algorithm
    # 1. Check if a valid timetable is possible with the given constraints
    # 2. Assign subjects and teachers to periods for each class
    # 3. Ensure all constraints are satisfied
    busy = {}


    return timetable


def display_timetable(timetable):
    """
    Display the generated timetable in a readable format.
    
    Args:
        timetable (dict): The generated timetable
    """
    # TODO: Implement timetable display logic
    # Display the timetable for each class
    # Display the timetable for each teacher
    pass


def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    # TODO: Implement validation logic
    # Check if all classes have their required number of periods for each subject
    # Check if teachers are not double-booked
    # Check if teachers are only teaching subjects they can teach
    
    return False, "To be implemented"


def main():
    """
    Main function to generate and display the timetable.
    """
    print("Generating school timetable...")
    
    # Generate the timetable
    timetable = generate_timetable()
    
    # Validate the timetable
    is_valid, message = validate_timetable(timetable)
    
    if is_valid:
        # Display the timetable
        display_timetable(timetable)
    else:
        print(f"Failed to generate valid timetable: {message}")


if __name__ == "__main__":
    main()
