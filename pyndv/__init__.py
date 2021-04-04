"""
Lib load modules for pyndv
"""


import logging

from pyndv import core

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


__all__ = core
