import sqlite3
import os
from pathlib import Path
import webbrowser as web
import time
import pyautogui as pg


def sql_to_json(path):
    base_dir = Path(__file__).resolve(strict=True).parent.parent
    new_path = base_dir / path
    if os.path.isfile(new_path):
        pass
    else:
        return "Incorrect Path"

    connection = sqlite3.connect(new_path)

    json = []

    cursor = connection.cursor()
    cursor.execute("SELECT * from main_index;")
    connection.commit()
    temp = cursor.fetchall()
    for items in temp:
        if len(items) == 6:
            dic = {'id': items[0], 'firstname': items[1], 'lastname': items[2], 'dob': items[3], 'email': items[5],
                   'phone_number': items[4]}
            json.append(dic)

    return json


class Whatsapp:
    def __init__(self, number, message='This is sent from Samuel Script'):
        self.number = number
        self.message = message

    def numcheck(self, number):
        if len(number) < 14 or number[0] != '+' or len(number) == 11 or len(number) < 11:
            if len(number) < 14 and len(number) == 11:
                temp = [char for char in number]
                temp[0] = '+234'
                new = ''.join(temp)
                return new
            elif number[0] != '+' or len(number) == 13:
                temp = [char for char in number]
                temp.insert(0, '+')
                return temp
            elif len(number) < 11 and len(number) < 14:
                return "Incorrect"
        else:
            return number

    def sendmsg(self, delay):
        number = self.numcheck(self.number)
        web.open('https://web.whatsapp.com/send?phone=' + number + '&text=' + self.message)
        time.sleep(delay)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        time.sleep(10)
        pg.press('enter')
        time.sleep(5)
        pg.hotkey('ctrl', 'w')

