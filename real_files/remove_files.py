'''Write a script “remove_files.py” that will look in the chapter 7 practices files
folder named “little pics” as well all of its subfolders. The script should
use os.remove() to delete any JPG file found in any of these folders if the file
is less than 2 Kb (2,000 bytes) in size.
You can supply the os.path.getsize() function with a full file path to return the
file's size in bytes. Check the contents of the folders before running your script to
make sure that you delete the correct files; you should only end up removing the
files named “to be deleted.jpg” and “definitely has to go.jpg” -
although you should only use the file extensions and file sizes to determine this.
If you mess up and delete the wrong files, there is a folder named “backup” that
contains an exact copy of the “little pics” folder and all its contents so that you
can copy these contents back and try again.'''

import os

myPath = "/home/alexpc/RL-learn/book1-exercises/chp09/practice_files/little pics"

def del_jpg_and_small(somePath):
    for current_folder, sub_folder, files in os.walk(somePath):
        print("current folder:")
        print(current_folder)
        print("in files:")
        print(files)
        for file in files:
            full_file_name = os.path.join(current_folder, file)
            print("now i see on {}".format(full_file_name))
            print("and it has size {} bytes".format(os.path.getsize(full_file_name)))
            full_file_name_tuple = os.path.splitext(full_file_name)
            if full_file_name_tuple[1] == ".jpg" and os.path.getsize(full_file_name) <= 2000:
                print("now remove file {}".format(full_file_name))
                os.remove(full_file_name)

del_jpg_and_small(myPath)