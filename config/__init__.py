from .default_config import DEFAULT_CONFIG, INTERNAL_CONFIG
import logging

CONFIG = {}

def load_config():
    global CONFIG
    logger = logging.getLogger('RPG_API.config')
    try:
        from .config import CONFIG as CUSTOM_CONFIG
        logger.info('Custom config file found')
    except Exception:
        logger.warning('No custom config file found')
        CUSTOM_CONFIG = {}
    finally:
        CONFIG = {**DEFAULT_CONFIG, **CUSTOM_CONFIG}
        CONFIG.update(INTERNAL_CONFIG)

