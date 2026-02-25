import logging

logger = logging.getLogger(__name__)

def divide(a, b):
    logger.info('divide called')
    return a / b

def divide_custom(a, b):
    logger.info('divide_custom called')

    if b == 0:
        logger.error('zero divide')
        raise ValueError('zero divide is forbidden')

    return a / b
