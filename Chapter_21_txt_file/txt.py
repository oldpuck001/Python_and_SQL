# txt_py.py

with open('somefile.txt', 'r+') as f:
    print('f.read(3)指令執行結果：')
    print(f.read(3))
    print('f.read()指令執行結果：')
    print(f.read())

    print('f.write(\'Hello, \')指令執行結果：略')
    f.write('Hello, ')
    print('f.write(\'World!\')指令執行結果：略')
    f.write('World!')

    print('f.seek(0)指令執行結果：略')
    f.seek(0)
    print('f.read()指令執行結果：')
    print(f.read())

    print('f.tell()指令執行結果：')
    print(f.tell())

    print('f.seek(0)指令執行結果：略')
    f.seek(0)
    print('f.readline()指令執行結果：')
    print(f.readline())
    print('f.readline(4)指令執行結果：')
    print(f.readline(4))

    print('f.seek(0)指令執行結果：略')
    f.seek(0)
    print('f.readlines()指令執行結果：')
    print(f.readlines())

    print('lines = [\'\\na1\\n\', \'b2\\n\', \'c3\']指令執行結果：略')
    lines = ['\na1\n', 'b2\n', 'c3']
    print('f.writelines(lines)指令執行結果：略')
    f.writelines(lines)

    print('f.seek(0)指令執行結果：略')
    f.seek(0)
    print('f.read()指令執行結果：')
    print(f.read())

with open('somefile.txt') as f:
    for line in f:
        print('循環指令執行結果：')
        print(line, end='')