import logging


class CustomFormatter(logging.Formatter):
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Log:
    def __init__(self, logger_name, file_name):
        self.logger_name = logger_name
        self.fmt = '%(asctime)s | %(name)s | %(levelname)s: %(message)s'
        # Create stdout handler for logging to the console (logs all five levels)
        self.stdout_handler = logging.StreamHandler()
        self.stdout_handler.setLevel(logging.DEBUG)
        self.stdout_handler.setFormatter(CustomFormatter(self.fmt))
        self.file_name = file_name
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel("INFO")
        self.file_handler = logging.FileHandler(self.file_name)
        self.file_handler.setFormatter(logging.Formatter(self.fmt, datefmt='%m/%d/%Y %I:%M:%S%p'))
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stdout_handler)
