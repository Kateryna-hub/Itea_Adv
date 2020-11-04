from functools import wraps
import requests
import time

def repeat(number=2):

    def _repeat(func):
        print(func.__name__)

        @wraps(func)
        def wrapper(host_):
            total: float = 0.0
            for i in range(number):
                t_time = time.time()
                result = func(host_)
                tt_time = (time.time() - t_time)
                print(f'time = {tt_time}')
                total += tt_time
            return result, total

        return wrapper

    return _repeat



@repeat(10)
def connected(host_):
    response = requests.get(host_)
    return response.ok



result = connected('http://google.com')
print(result)
