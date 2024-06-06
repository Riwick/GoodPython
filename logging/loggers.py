import logging

# logging.basicConfig(level=logging.DEBUG)  # change debugging level to the lowest
# logging.basicConfig(level=logging.DEBUG, filename="mylogs.log")  # we write our logs to file

# we added some formatting for our logs
# logging.basicConfig(level=logging.DEBUG, filename="mylogs.log", format="%(levelname)s (%(asctime)s) - %(message)s")

# added encoding
# logging.basicConfig(level=logging.DEBUG, filename="mylogs.log", format="%(levelname)s (%(asctime)s) - %(message)s",
#                     encoding="utf-8")

# added filemode like in open function
logging.basicConfig(level=logging.DEBUG, filename="mylogs2.log", format="%(levelname)s (%(asctime)s) - %(message)s",
                    encoding="utf-8", filemode="w")

logging.debug("Debug")  # output to terminal
logging.info("Info")  # output to terminal
logging.warning("Warning")  # output to terminal
logging.error("Error")  # output to terminal
logging.critical("Critical")  # output to terminal

try:
    10 / 0
except ZeroDivisionError:
    logging.error("You can't divide by zero")


# creating new logger
logger = logging.Logger(name="Some Logger")

logger.info("Some info from new logger")

# handler for logger. It's handle our exceptions
handler = logging.FileHandler(filename="mylogs2.log", encoding="utf-8")

# formatter for logger. It's format our exceptions
formatter = logging.Formatter(fmt="%(name)s: %(levelname)s (%(asctime)s) - %(message)s")

# add our handler and formatter to logger
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Some log with handler and formatter")
