from sys import exit


def pretty_error_message(e):
    custom_error(e)

def custom_error(e):
    print("==[ ERROR ]===>", e)
    exit(1)