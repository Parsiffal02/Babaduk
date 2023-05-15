import os
file = 'C:/Users/mrgor/OneDrive/Рабочий стол/код/'
file_generator = os.walk(file)
for path_from_top, subdirs, files in file_generator:
    for s in subdirs:
        print(s)
        print(os.listdir(path_from_top + "/" + s))
        print()