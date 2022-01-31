import hashlib


def signup_service(uname, password):
    f = open("userbase.txt", "r+")

    uuid = hashlib.sha256(uname.encode())
    pass_id = hashlib.sha256(password.encode())

    lines = f.read().splitlines()
    for line in lines:
        if uuid.hexdigest() in line:
            print("User id already exists! ")
            return 0
    f.write(uuid.hexdigest() + ", " + pass_id.hexdigest() + "\n")
    f.close()
    return 1


def login_service(uname, password):
    stored_password = ""
    uuid = hashlib.sha256(uname.encode())
    pass_id = hashlib.sha256(password.encode())
    print(pass_id.hexdigest())
    with open("userbase.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            if uuid.hexdigest() in line:
                stored_password = line.split(", ")[1]
    print(stored_password)
    if stored_password == pass_id.hexdigest():
        print("Login Successful")
        return 1
    else:
        print("Invalid username or password")
        return 0


if __name__ == '__main__':
    signup_service("sachin123", "pass123")
