import logging

# setting up the logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("app1.log"), logging.StreamHandler()],
)

# creating logger

logger = logging.getLogger("ArithmeticApp")


def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result


def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result


def multi(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result


def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Dividing by zero")
        return None


add(10, 20)
sub(20, 10)
multi(20, 30)
div(20, 10)
