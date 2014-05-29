import pandas

def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    00:00:00 (hour:minutes:seconds)
    
    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21
        
    Please return hour as an integer.
    '''
    
    n = 0
    hour = ""

    for char in time:
        hour = hour + char
        n = n + 1

    if hour[0] == "0":
        hour = int(hour[1:2]) 
    else:
        hour = int(hour[:2]) 
    
    return hour

time_to_hour("00:00:00")
time_to_hour("01:11:11")
time_to_hour("21:12:12")


