#Email Slicer:

def email_slicer(email):
    try:
        username, domain = email.split('@')
        return f"Username: {username}\nDomain: {domain}"
    except ValueError:
        return "Invalid email address! Please enter a valid email."

# Get user input
email = input("Enter your email address: ").strip()
print(email_slicer(email))
