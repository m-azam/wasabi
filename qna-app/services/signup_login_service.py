import hashlib
import csv
from datetime import date
import pandas as pd

column_names = ['username', 'password', 'score', 'score_date', 'school_id']


def signup_service(uname, password):
    pass_id = hashlib.sha256(password.encode())
    df = pd.read_csv('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv', names=column_names)
    usernames = df['username']
    print(usernames)
    if uname in usernames.tolist():
        print('username already exists')
        return 0
    row_entry = [uname, pass_id.hexdigest(), '', '', '']
    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row_entry)
    return 1


def login_service(uname, password):
    stored_password = ""
    pass_id = hashlib.sha256(password.encode())
    with open("/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv") as f:
        lines = f.read().splitlines()
        for line in lines:
            if uname in line:
                stored_password = line.split(",")[1]
    if stored_password == pass_id.hexdigest():
        print("Login Successful")
        return 1
    else:
        print("Invalid username or password")
        return 0


if __name__ == '__main__':
    login_service('azam', 'hack123')
