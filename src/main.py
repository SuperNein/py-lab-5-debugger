import logging

from src.common.config import LOGGING_CONFIG
from src.services.simulation import Simulation


def main() -> None:
    """
    Main entry point for the application.
    :return:   None
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)

    print("Welcome to the Library!")
    seed = input("Enter seed: ")
    if seed.isnumeric():
        seed = int(seed)
    else:
        seed = None
    simulation = Simulation(logger, seed)

    steps = int(input("Enter number of steps: "))
    simulation.run(steps)


if __name__ == "__main__":
    main()
