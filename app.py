from datetime import datetime
import sys
import logging



def main():
    print("My python code text")
    print("Execution time - BY ASIF ", datetime.now())
    logger.info('this is test for log main function')

if __name__ == "__main__":
    logger = logging.getLogger("general_log_test")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)
    main()
    logger.info('this is test for log end of code')
