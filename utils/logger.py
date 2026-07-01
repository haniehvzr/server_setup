#logger 

import logging

logging.basicConfig(
                    filename="logs/app.log",
                    filemode="a",
                    level= logging.INFO )

def log(msg):
    logging.info(msg)