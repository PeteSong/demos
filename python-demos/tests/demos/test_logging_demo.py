import logging

from demos.logging_demo import get_logger


def test_get_logger():
    logger = get_logger()
    logger.info("info from test_get_logger")
    logger.warning("warning from test_get_logger")
    logger.error("error from test_get_logger")
    logger.critical("critical from test_get_logger")
    logger.debug("debug from test_get_logger")
    assert logger is not None
    assert logger.name == "ROOT"
    assert logger.level == 20  # INFO level
    assert len(logger.handlers) == 2
    # assert logger.handlers[0].level == 20  # INFO level
    assert isinstance(logger.handlers[0], logging.FileHandler)
