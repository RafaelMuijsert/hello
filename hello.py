"""Test module used for dependency setup.

Copyright (C) 2024.
"""

import logging

logger = logging.getLogger(__name__)


def get_number() -> int:
    """Get a number.

    Returns:
        int: 12

    """
    return 12


def main() -> None:
    """Set up logger and get a number."""
    logging.basicConfig(level=logging.DEBUG)
    number = get_number()
    logger.info(number)


if __name__ == "__main__":
    _ = main()
