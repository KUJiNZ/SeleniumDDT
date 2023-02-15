import logging


class Log:
    def __init__(self, logger_name, file_name):
        self.logger_name = logger_name
        self.file_name = file_name
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel("INFO")
        self.file_handler = logging.FileHandler(self.file_name)
        self.formatter = logging.Formatter('%(asctime)s %(name)s%(levelname)s: %(message)s ',
                                           datefmt='%m/%d/%Y %I:%M:%S%p')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def get_Logger(self):
        return self.logger
