import os,sys
import time,subprocess
def exec_command(cmd):
    try:
        out = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, \
                               stderr=subprocess.PIPE, cwd=os.getcwd())
        out, err = out.communicate()
        print(str(out))
        return err
    except Exception as e:
        print("Error {} has occurred\n".format(e))
        os.system("ifconfig enp3s0 up")
        exit(0)
try:
    if len(sys.argv) > 1:
        if "txt" in sys.argv[1]:
            commands_file = sys.argv[1].strip()
    else:
        print('!!!!!!!!!!   Enter the correct name of text file  !!!!!!!!!!')
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
    print(' #######  Starting to disable internt and execute the commands   ####### ')
    os.system("ifconfig enp3s0 down")
    time.sleep(5)
    for command in commands:
        print('--------------- executing  command: '+str(command)+ '  --------------')
        error= exec_command(command)
        if error !="":
            raise Exception("There is an error")
    print('#######  All commands are executed and enabling the internet   ####### ')
    os.system("ifconfig enp3s0 up")
except Exception as e:
    print("Error {} is occurred".format(e))
    os.system("ifconfig enp3s0 up")
