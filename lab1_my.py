import time
from datetime import datetime

right_this_minute = datetime.today().minute

print(right_this_minute, 'minutes, division by 2 =>', right_this_minute % 2, sep=' ', end='\n\n')

if right_this_minute % 2 == 1:
    print('This minute seems a little odd.', end='\n\n')
else:
    print('Not an odd minute.', end='\n\n')

today = datetime.today().weekday()

if today == 5:
    print('Party!! It is Saturday', end='\n\n')
elif today == 6:
    print('Recover. It is Sunday', end='\n\n')
else:
    print('Work, work, work. It is', time.strftime("%A."), end='\n\n')

from os import getcwd

where_am_I = getcwd()

print(where_am_I)