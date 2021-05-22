import os

# count the number of ducks to be posted
duckCount = sum(len(files) for _, _, files in os.walk("/home/pi/duckbot/ducks/"))


dtoken = 'ODM4NTA4MjE1MDQ1MTkzNzM4.YI8HoQ.thm68HVaxFi8Cj86ZGnTumAavz0'
duckpath = '/home/pi/duckbot/ducks/'
status = [f'?duck: with {duckCount} ducks waiting to be posted!', '?8ball', '?swimmer']
