from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Group
from rich.align import Align
from rich.text import Text
from rich.layout import Layout
from rich.progress_bar import ProgressBar
from metrics.displaying_data import collect_dashboard_data


def usage_color(percent):
    if percent <= 50:
        r = int(255 * percent / 50)
        g = 255
    else:
        r = 255
        g = int(255 * (100 - percent) / 50)

    return f"#{r:02X}{g:02X}00"


def build_dashboard():
    data = collect_dashboard_data()

    cpu = data["cpu"]
    mem = data["memory"]
    disks = data["disks"]
    nets = data["network"]
    speed = data["speed"]
    uptime = data["uptime"]

    # ---------------- Header ---------------- #

    days = uptime.days
    hours, rem = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    header = Panel(
        Group(
            Align.center(Text("SERVER HEALTH MONITOR", style="bold cyan")),
            Align.center(Text(f"\nSystem Uptime : {days}d {hours}h {minutes}m {seconds}s", style="bold green")),
        ),
        border_style="cyan",
    )

    # ---------------- CPU ---------------- #

    cpu_table = Table.grid(padding=(0, 1))
    cpu_table.add_row(
        "Usage",
        ProgressBar(
            total=100,
            completed=cpu["usage"],
            complete_style=usage_color(cpu["usage"]),
            finished_style=usage_color(cpu["usage"]),
        ),
        " ",
        f"[{usage_color(cpu['usage'])}]{cpu['usage']:.1f}%[/]"
    )
    cpu_table.add_row("Cores       ", str(cpu["cores"]))
    cpu_table.add_row("Threads     ", str(cpu["logical_cores"]))

    cpu_panel = Panel(cpu_table, title="🖥 CPU", border_style="bright_blue")

    # ---------------- Memory ---------------- #

    mem_table = Table.grid(padding=(0, 1))
    mem_table.add_row(
        "Usage",
        ProgressBar(
            total=100,
            completed=mem["usage"],
            complete_style=usage_color(mem["usage"]),
            finished_style=usage_color(mem["usage"])
        ),
        " ",
        f"[{usage_color(mem['usage'])}]{mem['usage']}%[/]"
    )
    mem_table.add_row("Total       ", f"{mem['total']:.2f} GB")
    mem_table.add_row("Available   ", f"{mem['available']:.2f} GB")

    mem_panel = Panel(mem_table, title="💾 Memory", border_style="magenta")

    # ---------------- Disk ---------------- #

    disk_table = Table(expand=True)

    disk_table.add_column("Device", style="cyan")
    disk_table.add_column("Mount")
    disk_table.add_column("Used")
    disk_table.add_column("Total")
    disk_table.add_column("Free")

    for disk in disks:
        disk_table.add_row(
            disk["device"],
            disk["mountpoint"],
            f"[{usage_color(disk['usage_percent'])}]{disk['usage_percent']}%[/]",
            f"{disk['total_gb']:.2f} GB",
            f"{disk['free_gb']:.2f} GB",
        )

    disk_panel = Panel(disk_table, title="💽 Disk Usage", border_style="green")

    # ---------------- Network ---------------- #

    # Show only active interfaces (except loopback)
    active_nets = [
        net for net in nets
        if net["is_up"] and not net["interface"].lower().startswith("loopback")
    ]

    # If none are active, show all interfaces
    if not active_nets:
        active_nets = nets

    net_table = Table(expand=True, show_header=True)

    net_table.add_column("Interface", style="cyan", overflow="fold")
    net_table.add_column("IPv4", style="green")
    net_table.add_column("Speed", justify="right")
    net_table.add_column("Status", justify="center")

    for net in active_nets:
        ipv4 = net["ipv4"][0]["address"] if net["ipv4"] else "N/A"

        status = "[green]UP[/]" if net["is_up"] else "[red]DOWN[/]"

        net_table.add_row(
            net["interface"],
            ipv4,
            f"{net['max_speed_mbps']} Mbps",
            status,
        )

    net_panel = Panel(
        net_table,
        title="🌐 Network",
        border_style="yellow",
    )

    # ---------------- Speed ---------------- #

    speed_table = Table.grid()

    speed_table.add_row("Download   ", f"{speed['download_speed']:.2f} Mbps")
    speed_table.add_row("Upload     ", f"{speed['upload_speed']:.2f} Mbps")

    speed_panel = Panel(speed_table, title="⚡ Internet Speed", border_style="bright_magenta")

    footer = Align.center(
        Text("Refresh: 1 sec   |   Press CTRL+C to Exit", style="dim")
    )

    layout = Layout()

    # Main layout
    layout.split_column(
        Layout(header, size=5),
        Layout(name="body"),
        Layout(footer, size=1),
    )

    # Split body into left and right sections
    layout["body"].split_row(
        Layout(name="left", ratio=2),
        Layout(name="right", ratio=1),
    )

    # Left side: Disk above Network
    layout["left"].split_column(
        Layout(disk_panel, ratio=2),
        Layout(net_panel, ratio=2),
    )

    # Right side: CPU, Memory, Speed stacked vertically
    layout["right"].split_column(
        Layout(cpu_panel, size=6),
        Layout(mem_panel, size=5),
        Layout(speed_panel, size=4),
    )

    return layout