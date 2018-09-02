import os
import sys
import logging

from .env_stats import get_env_stats


def prepare_logger(logging_dir_path,
                   logging_file_name):
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    log_file_exist = False
    if logging_dir_path is not None and logging_dir_path:
        log_file_path = os.path.join(logging_dir_path, logging_file_name)
        if not os.path.exists(logging_dir_path):
            os.makedirs(logging_dir_path)
            log_file_exist = False
        else:
            log_file_exist = (os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0)
        fh = logging.FileHandler(log_file_path)
        logger.addHandler(fh)
        if log_file_exist:
            logging.info('--------------------------------')
    return logger, log_file_exist


def initialize_logging(logging_dir_path,
                       logging_file_name,
                       script_args,
                       log_packages,
                       log_pip_packages):
    logger, log_file_exist = prepare_logger(
        logging_dir_path=logging_dir_path,
        logging_file_name=logging_file_name)
    logging.info("Script command line:\n{}".format(" ".join(sys.argv)))
    logging.info("Script arguments:\n{}".format(script_args))
    logging.info("Env_stats:\n{}".format(get_env_stats(
        packages=log_packages.replace(' ', '').split(','),
        pip_packages=log_pip_packages.replace(' ', '').split(','))))
    return logger, log_file_exist
