# This script takes a folder with more than one folders creates a folder with combined files;
import json
import os
import shutil
from string import printable
import sys

cwd = os.getcwd()  # get the current working directory

if(len(sys.argv) > 1):
    args = sys.argv[1:]

else:
    args = {"targets": ["images", "labels"], "file_types": ["tif", "txt"]}


# print('Argument List:', args.get('file_types'))

    # parent_folder = cwd+'/datasets-3/'
parent_folder = '/Users/micka/Desktop/'+'/datasets-3/'
destination_folder = parent_folder+'/combined'

# we are interested to combine images and labels into separate files
# targets = ['images', 'labels']

targets = args.get('targets')
file_types = args.get('file_types')

if not os.path.isdir(destination_folder):
    os.makedirs(destination_folder)


def get_immediate_subdirectories(a_dir):
    # print('xxxxx',a_dir)
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


subdirectories = get_immediate_subdirectories(parent_folder)
subdirectories.remove('combined')

name_prefix = '0000'
naming_index = 1

for directory in subdirectories:
    # check if it has any of the specified target ;
    directory_path = parent_folder+directory
    # print('pathadfadf', path)
    folders = get_immediate_subdirectories(directory_path)

    check = any(item in targets for item in folders)

    if(check):  # folders contains one of the specificed targets;
        found_targets = targets and folders
        # print ("Found",found_targets)
        for target in found_targets:
            # create destination for files found under this target;
            target_index = targets.index(target)
            target_file_extension = file_types[target_index]
            if target == 'labels':
                print(target_index)
            target_path = os.path.join(directory_path, target)

            target_destination_folder = os.path.join(
                destination_folder, target)

            if not os.path.isdir(target_destination_folder):
                os.makedirs(target_destination_folder)

            files = [name for name in os.listdir(
                target_path) if os.path.isfile(os.path.join(target_path, name)) and name.endswith(target_file_extension)]

            # for each of these files create a copy and move it to the destination combined folder

            for file in files:
                file_path = os.path.join(target_path, file)

                file_extension = file[-4:len(file)]
                name_prefix = '0000'
                naming_index += 1

                new_name = os.path.join(
                    target_path, name_prefix+str(naming_index)+file_extension)

                shutil.copy(file_path, new_name)
                shutil.move(new_name, target_destination_folder)
