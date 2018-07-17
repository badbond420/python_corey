# to handle exception, let say you kept file name wrong

import logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    class my_exception(Exception):
        pass
        # Exception as e, here doesnt have enough info,
        # breaks if you want to print something
        # as its user defined exception, you know what and why it is
        # so always keep one except block with explaination
        # print str(e) is not recomended

try:
    fh = open("country.txt")
except FileNotFoundError as e:
    logger.error("Bad file name or file not exists")
except Exception as e:
    logger.error("something went wrong")
else:
    print(fh.read())
    fh.close()
finally:
    pass
    # release/clean some resources



