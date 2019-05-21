#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ValueError:
        return None
    finally:
        print("Inside Result: {}".format(result))
        return result
