import logging


def log(function):
    def wrapper(*args, **kwargs):
        logging.info("Executing function: %s", function.__name__)
        return function(*args, **kwargs)
    return wrapper