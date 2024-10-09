from logger import logging


def add(a, b):
    logging.info("This function is returning addition of two numbers")
    return a + b


print(add(10, 5))
