import functools
import logging


def get_readable_function_name(function_name: str):
    word_list: list[str] = function_name.split('_')
    word_list_capitals = map(lambda name : name.capitalize(), word_list)
    readable_name: str = " ".join(word_list_capitals)
    return readable_name

def log_test_results(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        function_name: str = get_readable_function_name(function.__name__)
        logging.info(f'Testing: {function_name}')
        try:
            function(*args, **kwargs)
            logging.info('Passed!')
        except AssertionError as error:
            logging.info('Failed!')
            raise
        except Exception as exception:
            logging.info(exception)
            raise
        finally:
            logging.info('-' * 30 + '\n')
    return wrapper

def log_test_class(class_tested: str):
    def decorator(cls):
        unit_test_class = getattr(cls, 'setUpClass', None)

        @classmethod
        def class_logger(cls_instance):
            logging.info(f'Testing class: {class_tested}')
            logging.info('-' * 30 + '\n')
            if unit_test_class:
                unit_test_class()

        cls.setUpClass = class_logger
        return cls
    return decorator