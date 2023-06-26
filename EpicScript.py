import byml
import os
import oead
import csv
import re

counter_epic = 0

with open ('./mainlist.csv') as weaps:
    wepreader = csv.reader(weaps)

    for row in wepreader:
        typeof = row[1].split('_')

        if typeof[1] == 'Shield' or typeof[1] == 'Bow':
            type_param = typeof[1]
        else:
            type_param = 'Weapon'
        
        type_param = type_param + 'Param'

        name = "Component/"+ type_param +"/" + str(row[1]) + ".game__component__"+ type_param +".bgyml"
        name_get = "Actor/"+ str(row[1]) +".engine__actor__ActorParam.bgyml"

        def replace(file):
            x = byml.Float(-200.0)
            y = byml.Float(0.0)
            z = y
            file.update({'SheathTransOffset': {'X': x, 'Y': y, 'Z': z}})
        
        with open('./example/' + str(row[1]) + '.pack', 'r+b') as weapon:
            sweapon = oead.Sarc(weapon.read())
            sarc_writer = oead.SarcWriter.from_sarc(sweapon)

            byml_list = []
            pattern = re.compile(typeof[0]+"_"+typeof[1]+'_' + "\d+\.game__component__"+type_param+"\.bgyml")
            for x in range (0, oead.Sarc.get_num_files(sweapon)+1):

                inside = str(oead.Sarc.get_file(sweapon, x))
                print(inside)
                print(typeof[0]+"_"+typeof[1]+'_' + "\d+\.game__component__"+type_param+"\.bgyml")
                

                if pattern.search(inside):
                    byml_list.append(inside)

            print(byml_list)
            if len(byml_list) == 1:
                true_final_name = name
            else:
                if byml_list[0].find(typeof[2]) == -1:
                    true_final_name = byml_list[0]
                else: 
                    true_final_name = byml_list[1]

            print(true_final_name)

            file = oead.Sarc.get_file(sweapon, true_final_name) #this used to be (sweapon, egaming)
            parser = byml.Byml(bytes(file.data))
            document = parser.parse()

            endi = str(oead.Sarc.get_endianness(sweapon))
            if endi == 'Endianness.Little':
                endi = 0
            else:
                endi = 1

            replace(document)
            
            if os.path.exists('./example/temp_bgyml.bgyml'):
                counter_epic += 1
                #print("Succuess", counter_epic)
            else:
                f = open('./example/temp_bgyml.bgyml', 'x')
                f.close()      
            

            with open('./example/temp_bgyml.bgyml', 'wb') as bm_file:
                writer = byml.Writer(document, be = bool(endi), version = 7)
                writer.write(bm_file)


            with open ('./example/temp_bgyml.bgyml', 'rb') as byml_file:
                gaming = byml_file.read()

                sarc_writer.files[true_final_name] = bytes(gaming) #this also used to be [egaming]
                save = sarc_writer.write()
                
                with open('./example/hbsfaf/' + str(row[1]) + '.pack', 'wb') as final:
                    final.write(save[1])
