import json
import requests
import sqlite3 as sq

hookURL = 'https://hook.eu1.make.com/wdnwoajce7fgkhylo8wiu6sznxo5kc3u'

data = {
    'quizTimeStart': '5.00',
    'quizTimeEnd': '11.00',
    'telegramUsername': '@testName',
    'RealName': 'Жора',
    'rightAnswers': '2'
}

# r = requests.post(hookURL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
base = sq.connect('check.db')
cursor = base.cursor()

name = cursor.execute('SELECT username FROM users').fetchone()
cursor.execute(f'INSERT INTO users VALUES ("asd", "passed")')
base.commit()
print(name is None)

print('ready')
