import logging
from functools import wraps

class Statistics():
    fn_call_counters = {}
    logger = logging.getLogger(__name__)

    def count_calls(name, print=True):
        Statistics.logger.info(f"count_calls")
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if name in Statistics.fn_call_counters:
                    Statistics.fn_call_counters[name] = Statistics.fn_call_counters[name] + 1
                else:
                    Statistics.fn_call_counters[name] = 1
                ret = fn(*args, **kwargs)
                if print:
                    Statistics.print_all()
                return ret
            return wrapper
        return decorator

    def print_all():
        Statistics.logger.info(f"Statistics:\n{Statistics.fn_call_counters}")

    