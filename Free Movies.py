import random
excuse = [
        "Password must be at least 41 characters long",
        "Password must contain at least one upper case number",
        "Password must contain at least two greek symbols",
        "Password must contain at least one emoji",
        "Password must contain either the name Steve or Austin",
        "Password must contain at least one hyperbole",
        "Password must conatin at least one your mom joke",
        "Password must contain at least one litterary device",
        "Password must contain your full name, address, and blood type",
        "Password must not conatin characters",
        "Password must be appropriate",
        "Password must conatain your mother's maiden name",
        "Password must not exceed 1 character in length",
        ]

print("This program will automatically get you free movies, just create create an account to get started")
remaining = 3
while remaining >= 0:
    input("input your username ")
    namefail = "Username already taken! Please try again"
    print (namefail)
    remaining = remaining - 1
pwcounter = 10
goodpw = 0
while goodpw != 1:
    pw = input("password: ")
    if pwcounter <= 0:
        goodpw = 1
    print (random.choice(excuse))
    pwcounter = pwcounter - 1

print("your account has been successfully created!")
print("please follow this URL to obatain your free movies: <REDACTED>")
