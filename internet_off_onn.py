import os,sys
import time
try:
    if len(sys.argv) > 1:
        if "txt" in sys.argv[1]:
            commands_file = sys.argv[1].strip()
    else:
        print("!!!!!!!!!!   Enter the correct name of text file  !!!!!!!!!!")
        exit(0)
    file1 = open(commands_file, 'r')
    Lines = file1.readlines()
    commands=[]
    for line in Lines:
        commands.append(str(line).strip())
except Exception as e:
    print("Error {} is occurred".format(e))
    exit(0)
try:
    print(" #######  Starting to disable internt and execute the commands   ####### ")
    os.system("ifconfig enp3s0 down")
    time.sleep(5)
    for command in commands:
        print('--------------- executing  command: '+str(command)+ '  --------------')
        os.system(command)
    print("#######  All commands are executed and enabling the internet   ####### ")
    os.system("ifconfig enp3s0 up")
except Exception as e:
    print("Error {} is occurred".format(e))
    os.system("ifconfig enp3s0 up")
