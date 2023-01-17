#!/usr/bin/python3
Data = []
pointer = 0
Functions = {
    'turkey' : 'print i am a turkey then loop 3 print goble goble'
}
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
import random
import time
def interactive(cmdd, point, returnB):
    if cmdd:
        cmd = cmdd

        for command in cmd:
            command = command.strip()
            if command.startswith('$DATA'):
                tcmd = command.split('$DATA')
                cmd[cmd.index(command)] = str(Data[int(tcmd[1])])
            elif command.startswith('$EVAL'):
                tcmd = command.split('$EVAL')
                cmd[cmd.index(command)] = str(interactive(Data[int(tcmd[1])].split(' '), 0, False)).strip()
        if str(None) in str(cmd):
            return cmd.remove(None)
        elif cmd[0] == 'rest':
            time.sleep(int(cmd[1]))
        elif cmd[0] == 'rand':
            return str(random.randint(int(cmd[1]), int(cmd[2])))
        elif cmd[0] == 'define':
            temp = ''
            for i in range(2, len(cmd)):
                temp+=str(cmd[i])+' '
            Functions[cmd[1]] = temp.strip()
        elif cmd[0] == 'length':
            temp = ''
            for i in range(1, len(cmd)):
                temp+=str(cmd[i])+' '
            return len(temp.strip())

        elif cmd[0] == 'incrament':
            point+=1
            return point
        elif cmd[0] == 'decrament':
            point-=1
            return point
        elif cmd[0] == 'math':
            okchars = '()1234567890-+*/. '
            temp = ''
            for i in range(1, len(cmd)):
                temp+=str(cmd[i])+' '
            temp = temp.strip()
            for x in temp:
                if not x in okchars:
                    print('UNSAFE MATH EXECUTION, ABORTING')
                    sys.exit()
            return eval(temp)
        elif cmd[0] == 'set':
            if cmd[1] == 'int':
                temp = ''
                for i in range(2, len(cmd)):
                    temp+=str(cmd[i])+' '
                print(str(interactive(temp.strip().split(' '), 0, True)))
                Data[point] = int(str(interactive(temp.strip().split(' '), 0, True)))
            elif cmd[1] == 'str':
                temp = ''
                for i in range(2, len(cmd)):
                    temp+=str(cmd[i])+' '
                Data[point] = str(temp.strip())
            elif cmd[1] == 'bool':
                Data[point] = bool(cmd[2])
        elif cmd[0] == 'location':
            return point
        elif cmd[0] == 'loop':
            for i in range(0, int(cmd[1])):
                temp = ''
                for i in range(2, len(cmd)):
                    temp+=str(cmd[i].strip())+' '
                print(interactive(temp.strip().split(' '), point, True))
            return point
        elif cmd[0] == 'print':
            temp = ''
            for i in range(1, len(cmd)):
                temp+=str(cmd[i])+' '
            return temp
        elif cmd[0] == 'is':
            temp = ''
            allowed = '1234567890-=+*/><! '
            for i in range(1, len(cmd)):
                temp+=str(cmd[i])+' '
            temp = temp.replace('True', '1').replace('False', '0')
            for char in temp:
                if not char in allowed:
                    print("UNSAFE IF EVALUATION, ABORTING")
                    sys.exit()
            return eval(temp)
        elif cmd[0] == 'if':
            if not cmd[2] == 'do':
                print('ERROR: DO STATEMEN REQUIRED')
            if cmd[1] == 'True':
                temp = ''
                for i in range(3, len(cmd)):
                    temp+=str(cmd[i])+' '
                point = interactive(temp, point, True)
        elif cmd[0] == 'data':
            if cmd[1] == 'int':
                Data.append(int(cmd[2]))
                return 'INTDATA ADRESS: '+str(len(Data)-1)
            elif cmd[1] == 'str':
                temp = ''
                for i in range(2, len(cmd)):
                    temp+=str(cmd[i])+' '
                Data.append(str(temp).strip())
                return 'STRDATA ADRESS: '+str(len(Data)-1)
            elif cmd[1] == 'bool':
                Data.append(bool(cmd[2]))
                return 'BOOLDATA ADRESS: '+str(len(Data)-1)
        elif cmd[0] == 'DATA':
            return Data[int(cmd[1])]
        elif cmd[0] == 'out':
            return Data[point]
        elif cmd[0] == 'tape':
            return Data
        else:
            if str(cmd).strip() in Functions:
                code = Functions[cmd.strip()].split(' then ')
                for command in code:
                    print(interactive(command.split(' '), 0, True))
            else:
                print('''%s
    \033[1m Unknown command\033[0m \033[0m  [%s]
    \033[1m \033[93m Error at line\033[0m \033[0m  [%s]
    \033[1m \033[93m File:\033[0m \033[0m  [%s]
    \033[1m \033[93m Path:\033[0m \033[0m  [%s]
    %s''' % (bcolors.FAIL, cmd, 'LOCALLINE', 'LOCAL FILE', os.getcwd(), bcolors.ENDC))
            if returnB:
                pointer = point

    pointer = point
if not 1 < len(sys.argv):
    print('''\033[91m\033[1mPLEASE SPECIFY A OPTION 
    [ -H HELP ON UNKNOWN COMMANDS  ____
    | -I INTERACTIVE MODE         ///\\\\\\
    [ -F FILE READ MODE            |[]|
                                   [||]
                                  ///\\\\\\
                                  [/[]\\]
                                  {____}
                                 [||[]||]
                                //|====|\\\\
    \033[0m''')
    sys.exit()
else:
    if sys.argv[1] == '-H':
        print('''
rest:
    Halts the process for a given amount of time in seconds
    Ex: `rest 10`
    Ex: `rest $DATA01

rand:
    Outputs a sudo random number based on one minimum and one maximum
    Ex: `rand 1 100`
    Ex: `rand $DATA0 $DATA1`

define:
    Creates a function that will be executed when the name is sent as a command different lines are seperated by a 'then' statement
    Ex: `define FunctionName print hello then print world then print !`
    Then if you call the function: `FunctionName` the code will be executed

length:
    Outputs the length of a given argument
    Ex: `length abcdefg`

tape:
    Outputs the current DATA tape
    Ex: `tape`

out:
    Outputs the current data block at the pointer index
    Ex: `out`

DATA or $DATA<data index>:
    Outputs the data block of the given argument
    Ex: `DATA 0`
    Ex: `print $DATA0`


data:
    Establishes a new data block of either type int (integer), str (string), or a bool (boolean)
    Ex: `data int 2`
    Ex: `data str hello world`
    Ex: `data bool True`

if:
    Test if a given data block or argument is True if it is true it will excute a set of commands
    Ex: `if True do out`
    Ex: `if $DATA0 do out`

is:
    Test if a given expression is true or false
    Ex: `is 1 + 1 == 2`
    Ex: `is 9 > 9`
    It is also possible to assign the output of these commands to a boolean data block
    Ex: `data str is 1 + 1 == 2` then `data bool $EVAL0`

print:
    Outputs text or data blocks from given arguments
    Ex: `print hello world`
    Ex: `print $DATA0`
    Ex: `print $EVAL0`

loop:
    Loops and does something multiple time based on given arguments
    Ex: `loop 3 print hewo`
    Ex: `loop $DATA0 print hewo`
    Ex: `loop $DATA0 print $DATA0`

location:
    Outputs the current pointer index
    Ex: `location`

set:
    Sets the current data block at the pointer index to a different value based on given arguments
    Ex: `set int 420`
    (Note, that when setting the int data type the value it is set to is first evaluated)
    Ex: `set bool True`
    Ex: `set str Hello, World`

math:
    Evaluates a math equasion from a given set of arguments
    Ex: `math 1 + 1`
    (Spaces are optional seing as the mathmatical operations are ran through python3)
    All allowed operators are:  + - * / and ()

decrament:
    Decraments the pointer by a value of 1
    Ex: `decrament`

incrament:
    Incraments the pointer by a value of 1
    Ex: `incament`

$EVAL:
    Evals a pice of code from a string given as an argument
    Ex: `data str print hello world` then `$EVAL0`
    (Note, code no longer prints the value. The output of this code will be an error saying there is no command named hello!)
        ''')
    if sys.argv[1] == '-I':
            print('''
    %s  ___       ___       ___       ___       ___       ___       ___       ___   
     /\  \     /\  \     /\__\     /\__\     /\__\     /\  \     /\__\     /\  \  
     \:\  \   _\:\  \   /:| _|_   |::L__L   /:/  /    /::\  \   /:| _|_   /::\  \ 
    %s%s /::\__\ /\/::\__\ /::|/\__\  |:::\__\ /:/__/    /::\:\__\ /::|/\__\ /:/\:\__|
    /:/\/__/ \::/\/__/ \/|::/  /  /:;;/__/ \:\  \    \/\::/  / \/|::/  / \:\:\/__/
    \/__/     \:\__\     |:/  /   \/__/     \:\__\     /:/  /    |:/  /   \::/  / 
            %s%s   \/__/     \/__/               \/__/     \/__/     \/__/     \/__/  
    ''' % (bcolors.WARNING, bcolors.ENDC, bcolors.OKCYAN, bcolors.ENDC, bcolors.FAIL))
            cmdindex = 0
            cmd = ['']
            while cmd[0] != 'end()':
                cmd = input('>>> %s' % (bcolors.ENDC)).split(' ')
                cmdindex+=1
                print(interactive(cmd, pointer, True))
    if sys.argv[1] == '-F':
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
            print(file)
            for command in file:
                print(interactive(command.strip().split(' '), pointer, True))
        readfile(sys.argv[2])