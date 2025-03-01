import functools
import logging
from enum import Enum


class LoggingColors(Enum):
    BOLD_RED: str = '\033[1;31m'
    BOLD_GREEN: str = '\033[1;32m'
    RESET: str = '\033[0m'
    BOLD_WHITE: str = '\033[1;37m'
    UNDERLINE: str = '\033[4m'
    BOLD_YELLOW: str = '\033[1;33m'


def get_readable_function_name(function_name: str):
    word_list: list[str] = function_name.split('_')
    word_list_capitals = map(lambda name : name.capitalize(), word_list)
    readable_name: str = " ".join(word_list_capitals)
    return readable_name

def log_test_results(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        function_name: str = get_readable_function_name(function.__name__)
        logging.info(f'Testing: {LoggingColors.BOLD_WHITE.value}'
                     f'{function_name}{LoggingColors.RESET.value}')
        try:
            function(*args, **kwargs)
            logging.info(f'{LoggingColors.BOLD_GREEN.value}'
                         f'Passed!{LoggingColors.RESET.value}')
        except AssertionError as error:
            logging.info(f'{LoggingColors.BOLD_RED.value}'
                         f'{LoggingColors.UNDERLINE.value}'
                         f'Failed!{LoggingColors.RESET.value}')
            raise
        except Exception as exception:
            logging.info(exception)
            raise
        finally:
            log_seperator()

    return wrapper

def log_test_class(class_tested: str):
    def decorator(cls):
        unit_test_class = getattr(cls, 'setUpClass', None)

        @classmethod
        def class_logger(cls_instance):
            logging.info(f'Testing class: {LoggingColors.BOLD_YELLOW.value}'
                         f'{class_tested}{LoggingColors.RESET.value}')
            log_seperator()
            if unit_test_class:
                unit_test_class()

        cls.setUpClass = class_logger
        return cls
    return decorator

def log_seperator():
    logging.info('-' * 50 + '\n')