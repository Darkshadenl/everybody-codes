# main.py
import sys, re
from app.model.dataHandle import data

def handleNameArg(searchValue = ""):
    numberPattern = '(?<=[A-Z]{3}-[A-Z]{2}-)\d{3}'
    
    d = data
    filtered = filter(d, searchValue)
    
    for row in filtered:
        nr = re.search(numberPattern, row['Camera'])
        if nr:
            print(f"{nr.group(0)} | {row['Camera']} | {row['Latitude']} | {row['Longitude']}")


def filter(reader, searchValue):
    filtered = []
    pattern = f'{searchValue}'
    for row in reader:
        txt = row['Camera']
        match = re.search(pattern, txt)
        if (match):
            filtered.append(row)
    return filtered    


def validateOperation(arg):
    for key, value in validArguments.items():
        if arg == key:
            return value
  

def extractOperationArgument(arguments):
    operation = None
    argument = None
    index = 1           # starting at 1 because first argument is always 'main.py'
    opPattern = '--[a-z]+'
    argPattern ='[a-zA-Z]*'
    
    while(operation == None and argument == None or index != len(arguments)):
        op = arguments[index]
        arg = arguments[index + 1]
        o = re.search(opPattern, op)
        a = re.search(argPattern, arg)
        
        if o and a:
            operation = validateOperation(op)
            argument = arg
            break
        else:
            index += 1
            continue
    
    return operation, argument
          

if __name__ == "__main__":
    validArguments = {'--name': handleNameArg}  
    
    try:
        if len(sys.argv) > len(validArguments) + 2:
            raise Exception(f'Main only takes {len(validArguments)} argument(s)')
    
        operation, argument = extractOperationArgument(sys.argv)
        
        if (operation):
            operation(argument)
        else:
            raise Exception('No valid argument found')
    except Exception as e:
        print(str(e))  