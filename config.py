import os
import logging.config


LOG_CONF = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "stream": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "time_series": {
            "handlers": ["stream"],
            "level": os.getenv("DF_LOG_LEVEL", "DEBUG"),
        }
    },
}

logging.config.dictConfig(LOG_CONF)

CUR_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))
DATA_DIR = os.getenv('DATA_DIR',   os.path.join(BASE_DIR,'data'))

def hello():
    return "hi"

if __name__ =="__main__":
    print(DATA_DIR)