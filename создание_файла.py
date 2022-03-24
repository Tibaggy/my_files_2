with open('new_file', 'w+') as f:
    write_data = 'Hello world!!!'
    f.write(write_data)
    read_data = f.read()
    print(read_data)