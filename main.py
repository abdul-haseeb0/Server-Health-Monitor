from rich.live import Live
from utils.ui import build_dashboard
from utils.logs_config import get_logger
import time

logger = get_logger()


def main():
    logger.info("Starting Server Health Monitor")

    try:
        with Live(build_dashboard(), refresh_per_second=2, screen=False) as live:
            while True:
                live.update(build_dashboard())
                time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Closing Server Health Monitor")
        print("\nClosing Server Health Monitor...")


if __name__ == "__main__":
    main()