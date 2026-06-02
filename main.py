from metrics.displaying_data import print_cpu
from metrics.displaying_data import print_uptime
from metrics.displaying_data import print_memory
from metrics.displaying_data import print_disk
from metrics.displaying_data import header_banner
from rich.live import Live
import time


def main():
    print(header_banner())
    print("Live System Resource Usage\n")

    try:
        with Live("", refresh_per_second=2) as live:
            while True:
                dashboard = (
                    f"{print_cpu()}\n\n"
                    f"{print_uptime()}\n\n"
                    f"{print_memory()}\n\n"
                    f"{print_disk()}"
                )
                live.update(dashboard)

                time.sleep(1)

    except KeyboardInterrupt:
        print("Closing Server Health Monitor\n...")
        return

if __name__ == "__main__":
    main()