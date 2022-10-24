import logging
import os

class Logging:
    # LOGGING
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=os.environ.get("LOGLEVEL", "INFO"),
    )
    logger = logging.getLogger("route.response.time")
