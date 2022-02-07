import time


def count_time(func):
    """
    count the running time
    """
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        finish_time = time.time()
        print('总共耗时：{}s'.format(finish_time - start_time))

    return inner

