#!/usr/bin/python3
Data = []
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import os
import sys
def evaluate(command, point):
    cmd = command.split(' ')
    for lol in cmd:
        if lol.startswith('$'):
            tcmd = lol.split('$')
            cmd[cmd.index(lol)] = Data[int(tcmd[1])]
    if cmd[0] == 'incrament':
        point+=1
        print(point)
    elif cmd[0] == 'decrament':
        point-=1
        print(point)
    elif cmd[0] == 'set':
        if cmd[1] == 'int':
            Data[point] = int(cmd[2])
        elif cmd[1] == 'str':
            Data[point] = str(cmd[2])
        elif cmd[1] == 'bool':
            Data[point] = bool(cmd[2])
    elif cmd[0] == 'location':
        print(point)
    elif cmd[0] == 'loop':
        for i in range(0, int(cmd[1])):
            point = evaluate(cmd[2], point)
        print(point)
    elif cmd[0] == 'print':
        temp = ''
        for i in range(1, len(cmd)):
            temp+=str(cmd[i])+' '
        print(temp)
    elif cmd[0] == 'data':
        if cmd[1] == 'int':
            Data.append(int(cmd[2]))
            print('INTDATA ADRESS: '+str(len(Data)-1))
        elif cmd[1] == 'str':
            temp = ''
            for i in range(2, len(cmd)):
                temp+=cmd[i]+' '
            Data.append(str(temp).strip())
            print('STRDATA ADRESS: '+str(len(Data)-1))
        elif cmd[1] == 'bool':
            Data.append(bool(cmd[2]))
            print('BOOLDATA ADRESS: '+str(len(Data)-1))
    elif cmd[0] == 'DATA':
        print(Data[int(cmd[1])])
    elif cmd[0] == 'out':
        print(Data[point])
    elif cmd[0] == 'tape':
        print(Data)
    else:
        print('evaluation error')
    return point
def interactive():
    point = 0
    cmdindex = 0
    cmd = ['']
    while cmd[0] != 'end()':
        cmd = input('>>> ').split(' ')
        cmdindex+=1
        for command in cmd:
            if command.startswith('$'):
                tcmd = command.split('$')
                cmd[cmd.index(command)] = Data[int(tcmd[1])]
        if cmd[0] == 'incrament':
            point+=1
            print(point)
        elif cmd[0] == 'decrament':
            point-=1
            print(point)
        elif cmd[0] == 'set':
            if cmd[1] == 'int':
                Data[point] = int(cmd[2])
            elif cmd[1] == 'str':
                Data[point] = str(cmd[2])
            elif cmd[1] == 'bool':
                Data[point] = bool(cmd[2])
        elif cmd[0] == 'location':
            print(point)
        elif cmd[0] == 'loop':
            for i in range(0, int(cmd[1])):
                point = evaluate(cmd[2], point)
            print(point)
        elif cmd[0] == 'print':
            temp = ''
            for i in range(1, len(cmd)):
                temp+=cmd[i]+' '
            print(temp)
        elif cmd[0] == 'data':
            if cmd[1] == 'int':
                Data.append(int(cmd[2]))
                print('INTDATA ADRESS: '+str(len(Data)-1))
            elif cmd[1] == 'str':
                temp = ''
                for i in range(2, len(cmd)):
                    temp+=cmd[i]+' '
                Data.append(str(temp).strip())
                print('STRDATA ADRESS: '+str(len(Data)-1))
            elif cmd[1] == 'bool':
                Data.append(bool(cmd[2]))
                print('BOOLDATA ADRESS: '+str(len(Data)-1))
        elif cmd[0] == 'DATA':
            print(Data[int(cmd[1])])
        elif cmd[0] == 'out':
            print(Data[point])
        elif cmd[0] == 'tape':
            print(Data)
        else:
            print('''%s
    \033[1m Unknown command\033[0m \033[0m  [%s]
    \033[1m \033[93m Error at line\033[0m \033[0m  [%s]
    \033[1m \033[93m File:\033[0m \033[0m  [%s]
    \033[1m \033[93m Path:\033[0m \033[0m  [%s]
    %s''' % (bcolors.FAIL, cmd, cmdindex, 'LOCAL FILE', os.getcwd(), bcolors.ENDC))
    print('\nGoodbye')

if not 1 < len(sys.argv):
    interactive()
    print('\033[91m\033[1mPLEASE SPECIFY A FILE\033[0m')
    sys.exit()
else:
    def readfile(filename):
        file = open(os.getcwd()+'/'+filename, "r").read().replace('\n', '').split(';')
        while("" in file):
            file.remove('')
        def fail(command, line, fname):
            print('''%s
            \033[1m Unknown command\033[0m \033[0m  [%s]
            \033[1m \033[93m Error at line\033[0m \033[0m  [%s]
            \033[1m \033[93m File:\033[0m \033[0m  [%s]
            \033[1m \033[93m Path:\033[0m \033[0m  [%s]
            %s''' % (bcolors.FAIL, command, line, fname, os.getcwd(), bcolors.ENDC))
            sys.exit()
        point = 0
        for cmdd in file:
            cmd = cmdd
            cmd = cmd.split(' ')
            for lol in cmd:
                if lol.startswith('$'):
                    tcmd = lol.split('$')
                    cmd[cmd.index(lol)] = Data[int(tcmd[1])]
            if cmd[0] == 'incrament':
                point+=1
                print(point)
            elif cmd[0] == 'decrament':
                point-=1
                print(point)
            elif cmd[0] == 'set':
                if cmd[1] == 'int':
                    Data[point] = int(cmd[2])
                elif cmd[1] == 'str':
                    Data[point] = str(cmd[2])
                elif cmd[1] == 'bool':
                    Data[point] = bool(cmd[2])
            elif cmd[0] == 'location':
                print(point)
            elif cmd[0] == 'loop':
                temp = ''
                for i in range(2, len(cmd)):
                    temp+=str(cmd[i])+' '
                for i in range(0, int(cmd[1])):
                    point = evaluate(temp.strip(), point)
                print(point)
            elif cmd[0] == 'print':
                temp = ''
                for i in range(1, len(cmd)):
                    temp+=str(cmd[i])+' '
                print(temp)
            elif cmd[0] == 'data':
                if cmd[1] == 'int':
                    Data.append(int(cmd[2]))
                    print('INTDATA ADRESS: '+str(len(Data)-1))
                elif cmd[1] == 'str':
                    temp = ''
                    for i in range(2, len(cmd)):
                        temp+=cmd[i]+' '
                    Data.append(str(temp).strip())
                    print('STRDATA ADRESS: '+str(len(Data)-1))
                elif cmd[1] == 'bool':
                    Data.append(bool(cmd[2]))
                    print('BOOLDATA ADRESS: '+str(len(Data)-1))
            elif cmd[0] == 'DATA':
                print(Data[int(cmd[1])])
            elif cmd[0] == 'out':
                print(Data[point])
            elif cmd[0] == 'tape':
                print(Data)
            else:
                fail('cmd[0]', 'file.index(cmd[0])', 'sys.argv[1]')
    readfile(sys.argv[1])