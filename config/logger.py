import logging


def get_logger(logger_name):
    logging.basicConfig(
        # filename='logs/app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(logger_name)
