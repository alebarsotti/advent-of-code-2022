from time import time

from Utils.Color import print_color

SECONDS_THRESHOLD = 10


def timed_method(func):
    """
    Decorator that reports execution time
    :param func: function to wrap
    :return: function wrapper
    """

    def wrap(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        elapsed_time = end - start
        unit = 'milliseconds' if elapsed_time < SECONDS_THRESHOLD else 'seconds'
        elapsed_time = elapsed_time * 1000 if elapsed_time < SECONDS_THRESHOLD else elapsed_time
        elapsed_time = f'{elapsed_time:.2f}'
        print(f'Execution time: {print_color(f"{elapsed_time} {unit}")}')

        return result

    return wrap
