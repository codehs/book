# Import the pyyaml library
import yaml
import sys
import os


def start():
    import getpass
    print "SCRIPT USER"
    print getpass.getuser()
    os.system("git pull")
    os.system("python build_html.py introcs/setup/config.yaml introcs/build/book.html")
    print "Completed build from github."

if __name__ == "__main__":
    start()
