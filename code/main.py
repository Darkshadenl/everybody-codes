# main.py
import sys
import re


def handleNameArg():
    print('--name hiiaaa')

def validateArgument(arg):
    for key, value in validArguments.items():
        if arg == key:
            value()
            return
            

if __name__ == "__main__":
    
    validArguments = {'--name': handleNameArg}  
    
    if len(sys.argv) > len(validArguments) + 2:
        raise Exception(f'Main only takes {len(validArguments)} argument(s)')
    
    for arg in sys.argv:
        v = re.search('--[a-z]+', arg)
        if v:
            validateArgument(arg)
        