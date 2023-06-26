# What is this?
A Python 3.10.2 script for modyfing Weapon_xxx_y.pack files of Zelda: Tears of the Kingdom.

Specifically, this script goes through every weapon file in the game using a cvs file obtained and merged from the [TOTK Data Sheet](https://docs.google.com/spreadsheets/d/18pNtDx3z-8CwGJRmlW574xbQ6VphQOkvpZhClpOEVDA/edit#gid=114269320), it only changes the coordinates of `SheathTransOffset` to `{'SheathTransOffset': {'X': -200, 'Y': 0, 'Z': 0}}` inside the `Component/WeaponParam/Weapon_(typeofweapon)_(number).game__component__WeaponParam.bgyml` of course, it makes sure to modify this string depending on if it's a bow, spear, sword, or Lsword (2-Handed Sword).

# How do I use this?
To get this to run you first need to get your pack.zs files from your TOTK romfs dump, uncompress them using something like [ZStdTool](https://github.com/TotkMods/Totk.ZStdTool) to get `(name).pack` and put them in the `./example` folder, after that run `EpicScript.py`. Your files should now be in `./example/hbsfaf`.
They are still uncompressed so make sure to recompress them again to `(name).pack.zs`. Once that's done you can now put these files wherever you need to.

# Requirements:
(install with pip3)
- [oead](https://github.com/zeldamods/oead/)
- [byml-v2](https://github.com/zeldamods/byml-v2)


# Extra comments
The hardest part of making the script was making sure the right bgyml was being edited, sometimes, the weapons have a matching AND a non-matching bgyml to the pack name.
Why? Likely due to some weapons simply being copy pasted to work off of as a base, then have only some stats changed in the matching file, while having the usual values in the non-matching file. 
Most files follow the logic of something like: `Weapon_LSword_163.pack` --> value `SheathTransOffset` is in bgyml --> `Weapon_LSword_163.game__component__WeaponParam.bgyml`. HOWEVER, some weapons follow the logic of `Weapon_LSword_163.pack` ---> value `SheathTransOffset` is in bgyml --> `Weapon_LSword_032.game__component__WeaponParam.bgyml`. WHILE also having a `Weapon_LSword_163.game__component__WeaponParam.bgyml`
Took me a while to figure how to deal with that properly, given that you can't really know what the number of the weapon will be beforehand, only what the correct one is, I had some help from a friend to figure this write this one properly, but I did manage the idea of "Get both, Choose the one that DOESN'T match the pack name".
