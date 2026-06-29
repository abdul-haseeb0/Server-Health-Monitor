def shm_banner():
    text = [
        "\n"
        r"███████╗██╗  ██╗███╗   ███╗",
        r"██╔════╝██║  ██║████╗ ████║",
        r"███████╗███████║██╔████╔██║",
        r"╚════██║██╔══██║██║╚██╔╝██║",
        r"███████║██║  ██║██║ ╚═╝ ██║",
        r"╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝",
        "\n"
    ]

    start = (0, 255, 255)   # Cyan
    end = (0, 100, 255)     # Blue

    for i, line in enumerate(text):
        t = i / (len(text) - 1)
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)

        print(f"\033[38;2;{r};{g};{b}m{line}\033[0m")