import  os
import re

# Specify the directory containing the files
directory = "."

# loop through all the files in the directory
for filename in os.listdir(directory):

    # construct the full path of the file
    filepath = os.path.join(directory, filename)

    # check if the file is a regular file  (not a directory)
    if os.path.isfile(filepath):
        # remove the pattern
        new_name = re.sub("Assignment", "",filename)
        new_filepath = os.path.join(directory, new_name)

        os.rename(filepath, new_filepath)


