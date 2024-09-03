"""Template Main File."""

import getpass

from utils.logger import logger


class Greeting:
    """Template Greeting Class."""

    def __init__(self) -> None:
        """Class initialization."""
        self.greeting = f"Hello {getpass.getuser()}!!!"

    def greet(self) -> str:
        """Return a greeting string."""
        return self.greeting


if __name__ == "__main__":

    my_greet = Greeting()
    logger.info(my_greet.greet())
    print(my_greet.greet())

