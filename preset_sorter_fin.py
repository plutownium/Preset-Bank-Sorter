import os


def folder_lister(dir_with_folders):
    """Accepts a path as input. Returns a list of directories in that file.
    """
    dir_list = os.listdir(dir_with_folders)
    counter = 0
    for item in dir_list:
        if not os.path.isdir(os.path.join(dir_with_folders + item)):
            dir_list.remove(item)
            counter += 1
    print "Removed %s non-folder entries." % counter
    return dir_list


def file_counter(folder_name, check_subfolders=True):
    """Uses os.walk() to return the number of files within a directory.
    Optionally includes the files within sub-directories. On by default.
    """
    full_path = os.path.join(collection_path, folder_name)
    counter_list = []
    non_patch_files = []
    for root, dirs, patches in os.walk(full_path):
        for patch in patches:
            if patch[-5:] == ".nmsv":
                counter_list.append(patch)
            else:
                non_patch_files.append(patch)
        if check_subfolders:
            non_patch_files.append(dirs)
    return len(counter_list), non_patch_files



collection_directory = raw_input("Directory of your soundbanks? > ")
collection_path = os.path.normpath(collection_directory)
os.chdir(collection_path)


folder_collection = os.listdir(collection_path)
print len(folder_collection)
for folder in folder_collection:
    if not os.path.isdir(folder):
        folder_collection.remove(folder)
collection_dict = {}
for folder in folder_collection:
    full_path = os.path.join(collection_path, folder)
    files_total = file_counter(folder)[0]
    collection_dict[folder] = full_path, files_total
removable_folders = []
for key in collection_dict:
    if collection_dict[key][1] <= 20:
        removable_folders.append(collection_dict[key][0])
removable_folders.sort()
print "I'm deleting stuff by hand."
for item in removable_folders:
    print item
