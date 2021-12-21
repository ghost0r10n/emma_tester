import time
from functools import wraps
import psutil


class Emma(object):




    def result_should_be(self, result:any, should_be:any)->any:
        return result==should_be

    
    def metrics_function(self, function, args, kwargs):
        start = time.perf_counter()
        function(*args, **kwargs)
        end = time.perf_counter()
        return f"{end - start:0.10f}s"


    def metrics(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            elapsed_time = self.metrics_function(function)
            print(f"Execution time --> {elapsed_time}")
        return wrapper

    def unit_test(self, **kwargs):
        # Variables pre instansiated
        should_be = None
        metrics = None
        mem_usage = None
        if 'should_be' in kwargs:
            should_be = kwargs['should_be']
        if 'metrics' in kwargs and type(kwargs['metrics']) == bool:
            metrics = kwargs['metrics']
        if 'profile_mem' in kwargs and type(kwargs['profile_mem'])==bool:
            mem_usage = kwargs['profile_mem']


        def unit_test_function(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                print(f'RUNNING TEST ON --> {function.__name__}\n')
                result = function(*args, **kwargs)
                if should_be!=None and not self.result_should_be(result, should_be):
                    print("FAILED --> the result of the function is incorrect")
                    print(f"    SHOULD BE :  {should_be}")
                    print(f"    BUT IT WAS:  {result}\n") 
                
                if metrics:
                    elapsed_time = self.metrics_function(function, args, kwargs)
                    print(f"Execution time --> {elapsed_time}")
                
                if mem_usage:
                    usage_before = psutil.virtual_memory()
                    function(*args, **kwargs)
                    usage_after = psutil.virtual_memory()

                    usage_before_rounded = round(usage_before.available/1024)
                    usage_after_rounded = round(usage_after.available/1024)
                    print(usage_before_rounded)
                    print(usage_after_rounded)
                    print(f'DIFFERENCE AFTER RUNNING --> {usage_before_rounded-usage_after_rounded} KB')

                return function
            return wrapper
        return unit_test_function






