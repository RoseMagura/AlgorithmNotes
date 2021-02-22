import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    all_files = []
    matches = []
    print(path)
    for item in path:
        print(item)
        if os.path.isfile(item):
            print('file')
            if item.endswith(suffix):
                matches.append(item)
            continue

        elif os.path.isdir(item):
            enter_dir(item, suffix, matches, path)
        #     # level = 0
        #     # print(type(item))
        #     # # while os.path.isdir(item):

        #     print('directory')
        #     enter_dir(item)
            # os.chdir(item)
            # level += 1
            # item = os.listdir(os.getcwd())
            # #     print('listing files', os.listdir())
            # #     if os.path.isfile(item):
            # #         print('file')
            # #         if item.startswith(suffix):
            # #             matches.append(item)
            # #         continue
            # os.chdir('../')
    return matches

def enter_dir(folder, suffix, matches, path):
    if os.path.isdir(folder):
        os.chdir(folder)
        for item in os.listdir():
            print('PROCESSING', str(item))
            print(os.path.isfile(item))
            if os.path.isdir(item):
                enter_dir(item, suffix, matches, path)
            elif os.path.isfile(item):
                print('FILE', str(item))
                if item.endswith(suffix):
                    matches.append(item)
        os.chdir('../')
    return matches

here = os.listdir('.')
print(find_files('.c', here)) # Expect ['a.c', 'b.c', 'a.c', 't1.c']
print(find_files('.gitkeep', here)) # Expect ['.gitkeep', '.gitkeep']
print(find_files('.jar', here)) # Expect []
print(find_files('.c', os.listdir('./testdir/subdir2'))) # Expect []
