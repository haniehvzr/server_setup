#backup server

import shutil
from utils.logger import log


def backup ():
    
    log("backup started")
    shutil.make_archive("backup/backup","zip","project/test.txt")
    log("backup successfull")

