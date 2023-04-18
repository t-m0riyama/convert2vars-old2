# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import glob
import os
import sys
import logging.config
from logging import (CRITICAL, DEBUG, ERROR, INFO, WARN, Formatter,
                     StreamHandler, getLogger)

__version__ = "1.0"


class Logging(object):
    @classmethod
    def get_logger(cls, config, log_filename, enableDebug, logger_name):
        # configを指定されていれば、設定をロード
        if config:
            logging.config.dictConfig(config)
            logger = getLogger(logger_name)
        else:
            if log_filename == '':
                logging.basicConfig(
                    level=logging.INFO,
                    stream=sys.stdout,
                    format="%(message)s"
                )
            else:
                logging.basicConfig(
                    level=logging.INFO,
                    filename=log_filename,
                    format="%(message)s"
                )
            logger = getLogger('root')

        # debug出力が指定された場合は、ログレベルをDEBUGにセット
        if enableDebug:
            logger.setLevel(logging.DEBUG)
        return logger

    @classmethod
    def info(cls, logger, message):
        return logger.info(message) if logger is not None else None

    @classmethod
    def warn(cls, logger, message):
        return logger.warn(message) if logger is not None else None

    @classmethod
    def error(cls, logger, message):
        return logger.error(message) if logger is not None else None

    @classmethod
    def debug(cls, logger, message):
        return logger.debug('DEBUG: ' + str(message)) if logger is not None else None
