# Email slicer program

def emailProcess(email):
    #youtube@kenn3thx.dev
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@") + 1:] # ":" to get all the characters after it 

    return email_username, email_domain

def printMsg(email_username, email_domain):
    print(f"Email username: {email_username}; Email Domain: {email_domain} ")

def main():
    email = input("Please enter your email address: ").strip()
    email_username, email_domain = emailProcess(email)

    printMsg(email_username, email_domain)

if __name__ == "__main__": # If don't have this line, when we run example_05.py, the main() function in this line will be called in example_05.
    main()