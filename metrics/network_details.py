import psutil
import time

KB = 1024

def network_info():

    addresses = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    result = []

    for iface, addr_list in addresses.items():
        iface_data = {
            "interface": iface,
            "is_up": stats[iface].isup if iface in stats else False,
            "max_speed_mbps": stats[iface].speed if iface in stats else 0,
            "ipv4": [],
            "ipv6": []
        }

        for address in addr_list:
            try:
                family_name = address.family.name
            except AttributeError:
                continue

            if family_name == "AF_INET":
                iface_data["ipv4"].append({
                    "address": address.address,
                    "netmask": address.netmask
                })
            elif family_name == "AF_INET6":
                iface_data["ipv6"].append({
                    "address": address.address
                })

        result.append(iface_data)

    return result


def speed_info():

    old = psutil.net_io_counters()
    time.sleep(1)
    new = psutil.net_io_counters()

    upload_speed = (new.bytes_sent - old.bytes_sent) / KB
    download_speed = (new.bytes_recv - old.bytes_recv) / KB

    return {
        "download_speed" : download_speed,
        "upload_speed" : upload_speed
    }