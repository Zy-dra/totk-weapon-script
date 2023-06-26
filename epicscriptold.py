import byml
import pyzstd
import os
import oead
import csv

with open ('./mainlist.csv') as weaps:
    wepreader = csv.reader(weaps)

    for row in wepreader:
        name = "Component/WeaponParam/" + str(row[1]) + ".game__component__WeaponParam.bgyml"
        name2 = str(row[1]) + ".game__component__WeaponParam.bgyml"
        opened_file = './example/' + str(row[1]) + '.pack'
        def replace(file):
            x = byml.Float(-200.0)
            y = byml.Float(0.0)
            z = y
            file.update({'SheathTransOffset': {'X': x, 'Y': y, 'Z': z}})

        with open('./example/' + str(row[1]) + '.pack', 'rb+') as weapon:
            sweapon = oead.Sarc(weapon.read())
            sarc_writer = oead.SarcWriter.from_sarc(sweapon)

            file = oead.Sarc.get_file(sweapon, name)
            parser = byml.Byml(bytes(file.data))
            document = parser.parse()

            endi = str(oead.Sarc.get_endianness(sweapon))
            if endi == 'Endianness.Little':
                endi = 0
            else:
                endi = 1

            replace(document)
            #print(document)
            
            if os.path.exists('./example/temp_bgyml.bgyml'):
                print("The file exists")
            else:
                f = open('./example/temp_bgyml.bgyml', 'x')
                f.close()      
            

            with open('./example/temp_bgyml.bgyml', 'wb') as bm_file:
                writer = byml.Writer(document, be = bool(endi), version = 7)
                writer.write(bm_file)


            with open ('./example/temp_bgyml.bgyml', 'rb') as byml_file:
                gaming = byml_file.read()

                sarc_writer.files[name] = bytes(gaming)
                save = sarc_writer.write()
                weapon.write(save[1])