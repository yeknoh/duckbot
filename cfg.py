import os

# count the number of ducks to be posted
duckCount = sum(len(files) for _, _, files in os.walk(""))

# Discord Developer API token
dtoken = ''
# Path to duck folder
duckpath = ''
# Discord game presence
status = [f'?duck: with {duckCount} ducks waiting to be posted!', '?8ball']
