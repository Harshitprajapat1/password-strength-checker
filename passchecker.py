import re

def password_length(passwd):
    if len(passwd) < 8:
        print("Password must be at least 8 characters")
        return False
    return True

def password_strength(passwd):
    strength = 0
    if re.search(r"[A-Z]", passwd):
        strength += 1
    if re.search(r"[a-z]", passwd):
        strength += 1
    if re.search(r"\d", passwd):
        strength += 1
    if re.search(r"\W", passwd):
        strength += 1
    
    if strength < 4:
        if not re.search(r"[A-Z]", passwd):
            print("Add uppercase letter")
        
        if not re.search(r"[a-z]", passwd):
            print("Add lowercase letter")
        if not re.search(r"\d", passwd):
            print("Add number")
        if not re.search(r"\W", passwd):
            print("Add special character")
       
    return strength

def cracking_time(passwd):
    r = 0
    length = len(passwd)
    if re.search(r"[a-z]", passwd):
        r += 26 ** length

    # Checking for uppercase letters
    if re.search(r"[A-Z]", passwd):
        r += 26 ** length

    # Checking for digits
    if re.search(r"\d", passwd):
        r += 10 ** length

    # Checking for special characters
    if re.search(r"\W", passwd):
        r += 31 ** length

    if r == 0:
        print("Error: Invalid password format.")
        return None

    # Calculate cracking time in seconds
    time_in_seconds = r / 1000000000

    # Converting seconds to various time units
    time_in_minutes = time_in_seconds // 60
    time_in_hours = time_in_minutes // 60
    time_in_days = time_in_hours // 24
    time_in_weeks = time_in_days // 7
    time_in_months = time_in_days // 30  
    time_in_years = time_in_days // 365 
    
    if time_in_seconds<60:
        print(time_in_seconds,"seconds")
    elif time_in_minutes <60:
        print(time_in_minutes,"Minutes")
    elif time_in_minutes <60:
        print(time_in_minutes,"Days")
    elif time_in_hours <60:
        print(time_in_hours,"Hours")
    elif time_in_days <60:
        print(time_in_days,"Days")
    elif time_in_weeks <=7:
        print(time_in_weeks,"Week")
    elif time_in_months<30:
        print(time_in_months,"Month")
    else:
        print(time_in_years,"Years")
    
    
    if time_in_seconds<3600:
        print(f"Password {passwd}is very Weak")
    elif time_in_seconds<86400:
        print(f"Password {passwd}is Weak")
    elif time_in_seconds<604800:
        print(f"Password {passwd}is Moderate")
    elif time_in_seconds<7257600:
        print(f"Password {passwd}is strong")
    else:
        print(f"Password {passwd}is very strong")
while(True):
    passwd = input("Enter a password: ")
    if re.search(" ",passwd):
        print("Space not allowed")
    else:
        password_length(passwd)
        password_strength(passwd)
        cracking_time(passwd)
