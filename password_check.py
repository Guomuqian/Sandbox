import string
password = input("What's your password：")
dig = 0
ICase = 0
hCase = 0
punctuation = 0
if len(password) <= 8 :
    print("**")
else:
    for ch in password:
        if ch in string.digits:
            dig = 1
        elif ch in string.ascii_lowercase:
            ICase = 1
        elif ch in string.ascii_uppercase:
            hCase = 1
        elif ch in string.punctuation:
            punctuation = 1
    if dig + ICase + hCase + punctuation == 2:
        print("****")
    elif dig + ICase + hCase + punctuation == 3:
        print("*****")
    elif dig + ICase + hCase + punctuation == 4:
        print("******")