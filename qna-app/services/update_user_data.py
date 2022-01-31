import pandas as pd
import csv


def update_score(uname, score):
    df = pd.read_csv('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv')
    usernames = df['username']
    list = usernames.tolist()
    if uname not in list:
        return 0
    idx = list.index(uname)
    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv') as f:
        data = [row for row in csv.reader(f)]

    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv', 'w') as f:
        w = csv.writer(f)
        data[idx + 1][2] = score
        for row in data:
            w.writerow(row)
    return 1


def update_date(uname, date):
    df = pd.read_csv('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv')
    usernames = df['username']
    list = usernames.tolist()
    if uname not in list:
        return 0
    idx = list.index(uname)
    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv') as f:
        data = [row for row in csv.reader(f)]

    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv', 'w') as f:
        w = csv.writer(f)
        data[idx + 1][3] = date
        for row in data:
            w.writerow(row)
    return 1


def update_schoolid(uname, school_id):
    df = pd.read_csv('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv')
    usernames = df['username']
    list = usernames.tolist()
    if uname not in list:
        return 0
    idx = list.index(uname)
    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv') as f:
        data = [row for row in csv.reader(f)]

    with open('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/userbase.csv', 'w') as f:
        w = csv.writer(f)
        data[idx + 1][4] = school_id
        for row in data:
            w.writerow(row)
    return 1
