#import random
#rebot_name_1  = ('Lemon')
#start = ('German')
#end = ('Srija')

#rebot_name_2 = ('Ice')
#start = ('German')
#end = ('Srbija')

#rebot_name_3 =('Peach')
#start = ('German')
#end = ('Srbija')

#import random(f"{rebot_name_1},{rebot_name_2},{rebot_name_3}")

import random

rebot_name_1 = 'Lemon'
rebot_name_2 = 'Ice'
rebot_name_3 = 'Peach'


robot_list = [rebot_name_1, rebot_name_2, rebot_name_3]


chosen_robot = random.choice(robot_list)

print(f"Ausgewählter Roboter: {chosen_robot}")