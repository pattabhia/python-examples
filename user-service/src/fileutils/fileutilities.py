def exists(file):
    try:
        with open(file) as f:
            print('file exists')
    except IOError:
        print('file not accessible')
