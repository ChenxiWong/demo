import logging
import os.path
from logging import handlers

base_path = "logger_demo"


def get_app_log_handler(
        name: str,
        max_bytes: int = 1024 * 1024 * 100,
        backup_count: int = 5,
        logger_level=logging.DEBUG, **kwargs):
    app_log = logging.getLogger(name)
    file_path = os.path.join(base_path, name + ".log")
    rh = handlers.RotatingFileHandler(file_path, max_bytes, backup_count)
    dfs = '%Y-%m-%d %H:%M:%S %p'
    fs = ('%(asctime)s | %(levelname)s|pathname: %(pathname)s|module: %(module)s|funcName: %(funcName)s|lineno:'
          ' %(lineno)d|pid: %(process)d|tid: %(thread)d|msg: %(message)s')
    app_format = logging.Formatter(fs, dfs)
    rh.setFormatter(app_format)
    app_log.addHandler(rh)
    app_log.setLevel(logger_level)
    return app_log
