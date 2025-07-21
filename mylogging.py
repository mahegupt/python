import helper
import logging
import traceback

from helper import do_something
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
# logging.error("I am error")
do_something()

try:
    l = [1, 2, 4]
    print(l[2])
    k = 1/0
# except IndexError as e:
#     logging.error(e, exc_info=True)
except ZeroDivisionError as d:
    logging.error(d, exc_info=True)
    logging.error("This error is %s", traceback.format_exc())
