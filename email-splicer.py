def main():
    print("Welcome to the email splicer ")
    print("")
    email = input("Enter email address: ")
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
while True:
    main()