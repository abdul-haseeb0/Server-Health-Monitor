from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Group
from rich.align import Align
from rich.text import Text

from metrics.displaying_data import collect_dashboard_data
from utils.banner import shm_banner


def usage_color(percent):
    if percent >= 80:
        return "red"
    elif percent >= 60:
        return "yellow"
    return "green"


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
            Align.center(Text(f"System Uptime : {days}d {hours}h {minutes}m {seconds}s", style="bold green")),
        ),
        border_style="cyan",
    )

    # ---------------- CPU ---------------- #

    cpu_table = Table.grid(padding=(0, 1))
    cpu_table.add_row("Usage", f"[{usage_color(cpu['usage'])}]{cpu['usage']}%[/]")
    cpu_table.add_row("Cores", str(cpu["cores"]))
    cpu_table.add_row("Threads", str(cpu["logical_cores"]))

    cpu_panel = Panel(cpu_table, title="🖥 CPU", border_style="bright_blue")

    # ---------------- Memory ---------------- #

    mem_table = Table.grid(padding=(0, 1))
    mem_table.add_row("Usage", f"[{usage_color(mem['usage'])}]{mem['usage']}%[/]")
    mem_table.add_row("Total", f"{mem['total']:.2f} GB")
    mem_table.add_row("Available", f"{mem['available']:.2f} GB")

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

    net_table = Table.grid()

    for net in nets:
        ipv4 = net["ipv4"][0]["address"] if net["ipv4"] else "N/A"

        net_table.add_row("Interface", net["interface"])
        net_table.add_row("Status", "UP" if net["is_up"] else "DOWN")
        net_table.add_row("IPv4", ipv4)
        net_table.add_row("Speed", f"{net['max_speed_mbps']} Mbps")
        net_table.add_row("", "")

    net_panel = Panel(net_table, title="🌐 Network", border_style="yellow")

    # ---------------- Speed ---------------- #

    speed_table = Table.grid()

    speed_table.add_row("Download", f"{speed['download_speed']:.2f} Mbps")
    speed_table.add_row("Upload", f"{speed['upload_speed']:.2f} Mbps")

    speed_panel = Panel(speed_table, title="⚡ Internet Speed", border_style="bright_magenta")

    footer = Align.center(
        Text("Refresh: 1 sec   |   Press CTRL+C to Exit", style="dim")
    )

    return Group(
        header,
        Columns([cpu_panel, mem_panel], equal=True, expand=True),
        disk_panel,
        Columns([net_panel, speed_panel], equal=True, expand=True),
        footer,
    )