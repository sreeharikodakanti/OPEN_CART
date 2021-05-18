import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\logs_1.log",
        format='(asctime)%S::(levelname)%S::(message)%S',
        datefmt="%d::%m::%Y  %I::%M::%S       %P")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
