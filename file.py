#newfile

import filesystem
defaultRootStorage = filesystem._root_storage
defaultRootData = filesystem._root_data
#current_dir = str(defaultRootStorage)+'/'
current_dir = '/'
defaultRootData['username'] = input('username: ').split(' ')[0]
data = defaultRootData['username']+"@reistem"

while True:
    #cmd = input(f'{data}:{current_dir}> ')
    if current_dir == '/storage/' or current_dir == '/storage':
        cmd = input(f'{data}:> ')
    else:
        cmd = input(f'{data}:{current_dir}> ')
    #if cmd not in filesystem._root_bin:
    if cmd.startswith('ls'):
        cmd_parts = cmd.split(' ')
        show_contents = '-c' in cmd_parts
        verbose = '-v' in cmd_parts
        if verbose:
            print(defaultRootStorage)
        elif show_contents:
            for file in defaultRootStorage:
                print(f"{file}: {defaultRootStorage[file]}")
        else:
            for file in defaultRootStorage:
                print(file)
    elif cmd.startswith('mkf'):
        try:
            #print(filesystem)
            cmd_parts = cmd.split(' ', 2)
            filename = cmd_parts[1]
            contents = cmd_parts[2]
            if '/' in contents:
                print('/ is not allowed')
            #if filename in defaultRootStorage:
            #    print(filename+' file already exists, '+filename+'-(2) has been made')
            #    defaultRootStorage[filename+'-(2)'] = contents

            if filename in defaultRootStorage:
                # If it does, increment a counter until a unique filename is found
                counter = 2
                while f"{filename}-({counter})" in defaultRootStorage:
                    counter += 1
                # Create the new file with the unique filename
                defaultRootStorage[f"{filename}-({counter})"] = contents
                print(f"{filename!r} file already exists, '{filename}-({counter})' has been made")
            if filename == '-e':
                defaultRootStorage[contents] = ''

            else:
                defaultRootStorage[filename] = contents
            #print(filesystem.root)
            #print(defaultRootStorage)
        except IndexError:
            #print('invalid arguments provided, mkf [filename] [contents]')
            error_pos = len('mkf') + 1
            print(cmd)
            print(' ' * error_pos + '^' * (len(cmd) - error_pos) + '\ninvalid arguments provided, mkf [filename] [contents]')
            #print('invalid arguments provided, mkf [filename] [contents]')
    elif cmd.startswith('mkdir'):
        try:
            cmd_parts = cmd.split(' ')
            path = cmd_parts[1]
            current_storage = defaultRootStorage
            for dirname in path.split('/')[:-1]:
                if dirname not in current_storage:
                    current_storage[dirname] = {}
                current_storage = current_storage[dirname]
            current_storage[path.split('/')[-1]] = {}
        except IndexError:
            error_pos = len('mkdir') + 1
            print(cmd)
            print(' ' * error_pos + '^' * (len(cmd) - error_pos) + '\ninvalid arguments provided, mkdir [path]')
    elif cmd.startswith('del'):
        try:
            cmd_parts = cmd.split(' ')
            filename = cmd_parts[1]
            del defaultRootStorage[filename]
        except IndexError:
            print('invalid arguments provided, del [filename]')
        except KeyError:
            print('no such file, del [filename]')
    elif cmd == 'rootfs':
        try:
            for key in filesystem.root:
                print(key)
            def defineRoot(sector):
                print(filesystem.root.get(sector))
            defineRoot('/ultra')
            print(filesystem.root['/root'])
            print(filesystem._root_storage)
            value = input('value: ')
            print(filesystem.root[value])
        except KeyError:
            print(f'KeyError: {value!r} does not exist')
    elif cmd.startswith('cd'):
        try:
            cmd_parts = cmd.split(' ')
            path = cmd_parts[1]
            if path == '..':
                defaultRootStorage = filesystem._root_storage
                current_dir = '/'.join(current_dir.split('/')[:-1]) or '/'
            elif path == '/':
                defaultRootStorage = filesystem._root_storage
                current_dir = '/'
            elif path.startswith('/'):
                current_dir = '/'
                defaultRootStorage = filesystem._root_storage
                for dirname in path.split('/')[1:]:
                    if dirname in defaultRootStorage:
                        if isinstance(defaultRootStorage[dirname], dict):
                            defaultRootStorage = defaultRootStorage[dirname]
                            current_dir = f"{current_dir.rstrip('/')}/{dirname}"
                        else:
                            print(f"{dirname!r} is not a directory")
                            break
                    else:
                        print(f"no such directory: {dirname!r}")
                        break
            elif path in defaultRootStorage:
                if isinstance(defaultRootStorage[path], dict):
                    defaultRootStorage = defaultRootStorage[path]
                    current_dir = f"{current_dir.rstrip('/')}/{path}"
                else:
                    print(f"{path!r} is not a directory")
            else:
                print(f"no such directory: {path!r}")
        except IndexError:
            print('invalid arguments provided, cd [path]')
    elif cmd == 'pwd':
        print(current_dir)
    elif cmd.startswith('lookup'):
        try:
            cmd_parts = cmd.split(' ', 2)
            finder = cmd_parts[1]
            print(finder)
        except IndexError:
            pass
    elif cmd.startswith('reidit'):
        try:
            cmd_parts = cmd.split(' ')
            filename = cmd_parts[1]
            if filename in defaultRootStorage:
                print(' -- reidit editor -- ')
                previousData = defaultRootStorage[filename]
                nano = input(defaultRootStorage[filename])
                defaultRootStorage[filename] = f"{previousData}{nano}"
                
                #Default = "Default Data"
                #userInput = input("Give me some info: \n{} \r".format(Default))
                #userInput += Default[len(userInput):]
            else:
                print(f'{filename!r} file does not exist')
        except IndexError:
            print('specify file to edit')
    elif cmd.startswith('yes'):
        try:
            cmd_parts = cmd.split(' ', 2)
            tag = cmd_parts[1] or ('default')
            if tag == 'default':
                for i in range(100):
                    print('y')
            else:
                for i in range(100):
                    #print(tag)
                    print(' '.join(cmd_parts[1:]))
        except IndexError:
            for i in range(100):
                print('y')
