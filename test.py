import csv
import oead
import glob

counter = 0
g = 'Component/WeaponParam/Weapon_Spear_003.game__component__WeaponParam.bgyml'
g2 = 'Component/WeaponParam/Weapon_Spear_113.game__component__WeaponParam.bgyml'

with open ('./example/compressed/Weapon_Spear_113.pack', 'rb') as pack:
    sweapon = oead.Sarc(pack.read())

    for x in range(0, oead.Sarc.get_num_files(sweapon)+1):
        file = oead.Sarc.get_file(sweapon, x)
        gaming = str(file)
        if gaming == g or gaming == g2:
            counter += 1
            if counter == 2:
                gaming = g
                print(gaming)
