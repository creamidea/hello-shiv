import requests
from .utils import say


def main():
    version = requests.__version__
    say('requests@{}'.format(version))
