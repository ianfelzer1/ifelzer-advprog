def crash():
        '''\
        crash the Python interpreter...
        '''
        i = ctypes.c_char('a')
        j = ctypes.pointer(i)
        c = 0
        while True:
                j[c] = 'a'
                c += 1
        j
