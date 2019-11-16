# Placeholder for setup file
# file will interface with both gnome keyring and google to get an app password, if necessary, and store it
#https://github.com/kiwiz/gkeepapi/issues/20

import keyring

#keyring.set_password("keepUlauncher", "ybotspawn@gmail.com", "ComplexPasswordOfDeath")
gottenPassword = keyring.get_password("keepUlauncher", "ybotspawn@gmail.com")
print(gottenPassword)
