#pyter filesystem
#/ -> _

_root = {
    'sff':'',
    'sff1':['_root'],
    'sff2':['_root_storage', '_root_data', '_root_data', '__root_bin'],
    'sff3':['_root_ultra'],
}

_root_storage = {
}

_root_data = {
    'system':'reistem',
}

_root_bin = {
    #'main':['ls','ls2','mkf','mkdir','del','cd','pwd'],
    'ls':{
        '':'ls',
        'contents':'ls -c',
        'verbose':'ls -v',
    },
    'mkf':{
        '':'mkf [filename] [contents]',
        'empty':'mkf -e [filename]',
    },
    'mkdir':'mkdir [dirname]',
    'del':'del [filename]',
    'rootfs':'rootfs',
    'cd':'cd [dirname]',
    'pwd':'pwd',
    'reidit':'reidit [filename]',
    'yes':'yes',
}

_root_ultra = {
}

#-----------------------------------------------

root = {
    '/':'root',
    '/root':_root,
    '/storage': _root_storage,
    '/data': _root_data,
    '/bin': _root_bin,
    '/ultra': _root_ultra,
}

#-----------------------------------------------

#sff - source for filesystem


#root = '/'
#sRoot = ''
