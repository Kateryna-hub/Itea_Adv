from functools import wraps
import requests
import time

def repeat(number=2):

    def repeat_(func):
        #print(func.__name__)

        @wraps(func)
        def wrapper(*args):
            start_total_time = time.monotonic()
            dict_ = {}
            for i in range(number):
                start_every_call = time.monotonic()
                result = func(*args)
                every_call = '{:>.3f}'.format(time.monotonic() - start_every_call)
                key = 'Call' +str(i + 1)
                dict_[key] = every_call
            total_time = '{:>.3f}'.format(time.monotonic() - start_total_time)
            dict_['total time'] = total_time
            dict_['Name'] = func.__name__
            dict_['result'] = result
            #print('total time : {:>.3f}'.format(time.monotonic() - start_total_time))
            #print(f'Name function: {func.__name__}')
            return dict_

        return wrapper

    return repeat_


@repeat(5)
def connected(host_):
    response = requests.get(host_)
    return response.ok


@repeat(6)
def sum_(a, b):
    c = a + b
    return c

#result = sum_(2345678, 54321)
result = connected('http://google.com')
print(result)
for key, value in result.items():
    print('{0}: {1}'.format(key, value))
