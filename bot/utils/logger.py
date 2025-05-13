import logging
import colorlog


def setup_logger():
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    logging.getLogger('sqlalchemy.engine').propagate = False

    logging.getLogger('sqlalchemy.pool').setLevel(logging.DEBUG)

    
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "bold_red"
        }
    ))
    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )