# move_files
A simple python script that scans the Downloads directory and moves specific file type to specific directories.


Have a cluttered Downloads folder?
Run this script in order to move all the pictures,documents,music to their respective folders!

**Currently availaible for linux and windows systems **

Categorises into Pictures Documents and Music (support for more categories will be added if required).

Pictures will be moved to /home/$user/Pictures (c:\user\username\Pictures for windows) ,similarly documents , music to their respective folders.

Further file types can be added to existing files to widen support.

As a security measure this script *WILL NOT* access files located in any subdirectory unless explicitly stated.

__Known bugs:__
Ignores files if extension is not in lowercase standard encoding.

