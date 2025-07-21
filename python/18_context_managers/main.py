from contextlib import contextmanager

class MyContextManager():
    def __enter__(self):
        print("entering my context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting context")
        if exc_type:
            print(f"An exception occurred: {exc_type.__name__}: {exc_val}")
            return True # suppress the exception
        return False # propagate the exception

@contextmanager
def safe_division():
    print("starting safe division")
    try:
        yield
    except ZeroDivisionError as e:
        print(f"Caught a division error: {e}")
    finally:
        print("Cleaning up after division.")

def main():
    with MyContextManager() as c:
        raise(ValueError("LOFASZ"))

    with safe_division():
        result = 1 / 0  # Will raise ZeroDivisionError

if __name__ == '__main__':
    main()