import os
import glob

# File renaming utility

# Getting non class file paths from directory recursively
file_paths = glob.glob(r'C:\Users\admin\Documents\Work\Thesis\Artop\repo\artext\misc\artext-luna-2\**\*.*', recursive=True)
filtered_paths = list(filter(lambda file: ('.class' not in file and '.xtext' not in file), file_paths))
filtered_paths = list(filter(lambda file: ('swcd' in file), filtered_paths))

for file in filtered_paths:
    handle = open(file, 'r')
    try:
        text = handle.read()
    except:
        print('error: ', file)

    text = text.replace('swcd', 'sysd')
    text = text.replace('Swcd', 'Sysd')
    text = text.replace('SWCD', 'SYSD')
    
    handle.close()

    handle = open(file, 'w')
    handle.write(text)
    handle.close()

    file_name_orig = os.path.basename(file)
    file_path_orig = os.path.dirname(file)

    file_name_orig = file_name_orig.replace('swcd', 'sysd')
    file_name_orig = file_name_orig.replace('Swcd', 'Sysd')
    file_name_orig = file_name_orig.replace('SWCD', 'SYSD')
    
    file_path_new = os.path.join(file_path_orig,  file_name_orig)

    os.rename(file, file_path_new)
    print(file_path_new)
