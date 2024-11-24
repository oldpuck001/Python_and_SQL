# txt_py.py

with open('somefile.txt', 'r+') as f:
    print(f.read(3))
    print(f.read())

    f.write('Hello, ')
    f.write('World!')

    f.seek(0)
    print(f.read())

    print(f.tell())

    f.seek(0)
    print(f.readline())
    print(f.readline(4))

    f.seek(0)
    print(f.readlines())

    lines = ['\na1\n', 'b2\n', 'c3']
    f.writelines(lines)

    f.seek(0)
    print(f.read())

with open('somefile.txt') as f:
    for line in f:
        print(line, end='')