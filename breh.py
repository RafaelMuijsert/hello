"""Test module used for dependency setup.

Copyright (C) 2024.
"""

import logging

import requests

logger = logging.getLogger(__name__)


def get_ip() -> str:
    """Get public IP address.

    Returns:
        str: public IPv4 address.

    """
    response = requests.get("https://ipv4.icanhazip.com", timeout=5)
    return response.text


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
    ip = get_ip()
    logger.info(number)
    logger.info(ip)


if __name__ == "__main__":
    _ = main()
