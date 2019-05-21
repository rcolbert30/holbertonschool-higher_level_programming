#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
    finally:
        print("Inside Result: {}".format(result))
    return result
