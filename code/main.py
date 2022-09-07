# main.py
from argparse import ArgumentError
from msilib.schema import Error
import sys


def handleName():
    pass

validArguments = {'--name': handleName}


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    if len(sys.argv) > 2:
        raise Exception(f'Main only takes {len(validArguments)} argument(s)')