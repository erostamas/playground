import sys
sys.dont_write_bytecode = True

from app import create_app
from logging_config import setup_logging
import logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting simulation job service")
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=12345)


if __name__ == '__main__':
    main()