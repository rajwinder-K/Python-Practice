import getpass

users ={
    "RaaviKaur": "werydm#4%$bptyu",
    "abc123": "123456"
}

username = input("Username: ")
password = getpass.getpass("Password: ")

if username in users and users[username] == password:
    print("Login Successful")
else: 
    print("Invalid Username or Password")
