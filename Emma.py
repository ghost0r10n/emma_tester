import time
from functools import wraps



class Emma(object):




    def timer():
        #TODO This method will show the time of execution of the function
        pass

    def result_should_be(self, result:any, should_be:any)->any:
        return result==should_be

    def metrics(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            function(*args, **kwargs)
            end = time.perf_counter()
            print(f"Execution time --> {end - start:0.4f}")
        return wrapper

    def unit_test(self, **kwargs):
        if 'should_be' in kwargs:
            should_be = kwargs['should_be']
        if 'metrics' in kwargs:
            metrics = kwargs['metrics']
        def unit_test_function(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                print(f'RUNNING TEST ON --> {function.__name__}')
                result = function(*args, **kwargs)
                if not self.result_should_be(result, should_be):
                    print("FAILED --> the result of the function is incorrect")
                self.metrics(function)
                return function
            return wrapper
        return unit_test_function
