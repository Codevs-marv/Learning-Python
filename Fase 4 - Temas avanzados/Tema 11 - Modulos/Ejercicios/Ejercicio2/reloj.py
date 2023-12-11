import datetime
import time
import os


while True:
    os.system('cls')
    dt = datetime.datetime.now()
    print(f'{dt.hour}:{dt.minute}:{dt.second}')

    # dormir el programa durante 1 seg (para así consumir menos memoria)
    time.sleep(1)