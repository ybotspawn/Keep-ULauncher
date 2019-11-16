import gkeepapi
from pathlib import Path

# Build a mechanism to grab the creds
home = str(Path.home())
credfile = open(home + '/creds.txt','r') 
creds = credfile.readlines()
print(creds[0].replace(' ', '').replace('\n',''))
print(creds[1])


keep = gkeepapi.Keep()
success = keep.login(creds[0].replace(' ', '').replace('\n',''), creds[1])


note = keep.createNote('Todo', 'Eat breakfast')
note.pinned = True
note.color = gkeepapi.node.ColorValue.Blue
keep.sync()

