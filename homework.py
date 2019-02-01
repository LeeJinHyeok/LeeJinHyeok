from datetime import datetime
today=datetime.today()
print(datetime.today().strftime("%Y/%m/%d"))

from datetime import datetime
today=datetime.today()
print("Today is" + ' ' +datetime.today().strftime("%Y/%m/%d"))

import time
print("Today is {}/{}/{}".format(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday))

name= input("Enter your name:")

print(name)
