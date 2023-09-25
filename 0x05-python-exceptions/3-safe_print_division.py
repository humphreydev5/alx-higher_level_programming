#!/usr/bin/python3

def safe_print_division(a, b):
     try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Results: {}".format(div))
    return (div)
