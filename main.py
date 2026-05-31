from metrics.displaying_data import print_cpu
from metrics.displaying_data import print_uptime
from metrics.displaying_data import print_memory
from metrics.displaying_data import print_disk



print("Welcome to Server Health Monitor (SHM)\n")
print("Gathering Server Information...\n")

print_cpu()
print_uptime()
print_memory()
print_disk()