"""magicento.magicento: provides entry point main()."""
 
 
__version__ = "0.0.1"
 
 
import sys
 
 
def main():
    print("Executing magicento version {}.".format(__version__))
    print("List of argument strings: {}".format(sys.argv[1:]))
    print("Magic():\n{}".format(Magic()))
 
 
class Magic():
    pass
