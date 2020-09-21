from moodles import functions as func
import datetime
import time
import urllib3

# Run web-server


# gets json file from db

db_path = 'form/db.sqlite3'  # database path
json = func.sql_to_json(db_path)

# Checks while DOB is == today

today = str(datetime.date.today())
db_id = []

for item in json:
    if item['dob'] == today:
        db_id.append((item['firstname'], item['phone_number']))

# Send message

for identity in db_id:
    name = str(identity[0])
    phone_num = str(identity[1])
    message = "Happy Birthday {}".format(name)
    func.Whatsapp(phone_num,message).sendmsg(5)
    time.sleep(3)

