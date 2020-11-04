from functools import wraps
import requests
import time

def repeat(number=2):

    def _repeat(func):
        #print(func.__name__)

        @wraps(func)
        def wrapper(host_):
            start_total_time = time.time()
            for i in range(number):
                start_func_time = time.time()
                result = func(host_)
                print('time = {:>.3f}'.format(time.time() - start_func_time))
            print('total time : {:>.3f}'.format(time.time() - start_total_time))
            print(f'Name function: {func.__name__}')
            return result

        return wrapper

    return _repeat



@repeat(4)
def connected(host_):
    response = requests.get(host_)
    return response.ok



result = connected('http://google.com')
print(result)
