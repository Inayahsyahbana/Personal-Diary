# first_name = 'Lina'
# last_name = 'kim'
# full_name = f'{first_name}{last_name}'
# print(full_name)

from datetime import datetime
now = datetime.now()
today = datetime.now()
date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
print(date_time)