#server setup main

import argparse
import subprocess
from utils.logger import log
from backup.backup import backup
from colorama import Fore , Style




parser = argparse.ArgumentParser()
parser.add_argument("--setup" ,action="store_true")
parser.add_argument("--backup" ,action="store_true")

arg = parser.parse_args()

def run_bash (script):
    subprocess.run(["bash",script], check=True)


def main ():

    log("setup started")

    if arg.setup :

        try:
            run_bash("setup/setup.sh")
            print (Fore.GREEN+"setup is running ..."+Style.RESET_ALL)
            log("setup completed")
        except Exception as e:
            log(f"Error : {e}")


    elif arg.backup :

        try:
            backup()
            print (Fore.GREEN+"backup is running ..."+Style.RESET_ALL)
            log("backup completed")

        except Exception as e :
            log(f"Error : {e}")



    

if __name__ == "__main__":
    main()