import os

if os.path.exists('main.txt'):
    source = 'main.txt'
    dest = 'newfile.txt'
    os.rename(source, dest)
    print('Source Path Renamed To Destination Path Successfully')
else:
    print('The system cannot find the specified file path')