import random
import hashlib

# Level 1: Textual Password Authentication
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password, entered_password):
    return stored_password == hash_password(entered_password)

# Level 2: One-Time Password (OTP) Authentication
def generate_otp():
    return random.randint(100000, 999999)

def verify_otp(stored_otp, entered_otp):
    return stored_otp == entered_otp

# Level 3: Security Question Authentication
def verify_security_answer(stored_answer, entered_answer):
    return stored_answer.lower() == entered_answer.lower()

# Main function to run the three-level password system
def three_level_authentication():
    # Pre-defined user credentials
    stored_password = hash_password("secure_password")
    stored_security_answer = "my first pet"
    
    # Level 1: Password Verification
    entered_password = input("Enter your password: ")
    if not verify_password(stored_password, entered_password):
        print("Password incorrect! Access denied.")
        return False
    print("Password verified.")

    # Level 2: OTP Verification
    otp = generate_otp()
    print(f"Your OTP is: {otp}")  # In a real system, OTP would be sent via SMS or email
    entered_otp = int(input("Enter the OTP sent to you: "))
    if not verify_otp(otp, entered_otp):
        print("OTP incorrect! Access denied.")
        return False
    print("OTP verified.")

    # Level 3: Security Question Verification
    entered_answer = input("What was the name of your first pet? ")
    if not verify_security_answer(stored_security_answer, entered_answer):
        print("Security answer incorrect! Access denied.")
        return False
    print("Security answer verified.")
    
    # If all levels are passed
    print("Access granted.")

# Run the authentication system
three_level_authentication()
