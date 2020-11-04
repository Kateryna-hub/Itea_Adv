from functools import wraps
import requests
import time

def repeat(number):
    def _repeat(func):

        @wraps(func)
        def wrapper(host_):
            for i in range(number):
                result = func(host_)
                return result
        return wrapper
    return _repeat



@repeat(8)
def connected(host_):
    start_time = time.time()
    response = requests.get(host_)
    print(f'time, {(time.time() - start_time)}')
    print(response.status_code)
    print(connected.__name__)
    return response.ok


print(connected.__wrapped__('http://google.com'))
result = connected('http://google.com')
print(result)