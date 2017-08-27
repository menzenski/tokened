import logging
import logging.config

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
      'simple': {
        'class': 'logging.Formatter',
        'style': '{',
        'datefmt': '%I:%M:%S',
        'format': ('{levelname:8s}; {asctime:s}; '
                   '{name:<15s} {lineno:4d}; {message:s}')
      },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        }
    },
    'root': {
        'handlers': [
            'console'
        ],
        'level': 'INFO'
    }
}


def configure_logging():
    logging.config.dictConfig(logging_config)
