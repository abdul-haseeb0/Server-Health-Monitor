from metrics.displaying_data import print_cpu,print_uptime,print_memory,print_disk,get_network_details,get_speed,header_banner
from utils.logs_config import get_logger
from rich.live import Live
import time

logger = get_logger()


def main():
    print(header_banner())
    print("Live System Resource Usage\n")
    logger.info(f"Starting Server Health Monitor\n...")

    try:

        with Live("", refresh_per_second=2) as live:
            while True:
                dashboard = (
                    f"{print_cpu()}\n\n"
                    f"{print_uptime()}\n\n"
                    f"{print_memory()}\n\n"
                    f"{print_disk()}\n\n"
                    f"{get_network_details()}\n\n"
                    f"{get_speed()}"
                )
                live.update(dashboard)

                time.sleep(1)

    except KeyboardInterrupt:
        print("Closing Server Health Monitor\n...")
        logger.error("Closing Server Health Monitor Keyboard Interrupt\n...")

        return

if __name__ == "__main__":
    main()