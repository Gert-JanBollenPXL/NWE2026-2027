
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "172.16.18.2",
    "username": "student",
    "password": "pxl"
}

connection = ConnectHandler(**device)

output = connection.send_command("show ip interface brief")

interfaces = {
    "up": [],
    "down": [],
    "administratively down": []
}

for line in output.splitlines()[1:]:
    columns = line.split()

    if len(columns) < 6:
        continue

    name = columns[0]
    status = " ".join(columns[4:-1])
    protocol = columns[-1]

    if status == "administratively down":
        interfaces["administratively down"].append(name)
    elif status == "up" and protocol == "up":
        interfaces["up"].append(name)
    else:
        interfaces["down"].append(name)

for status, names in interfaces.items():
    print(f"\n{status.upper()}: {len(names)} interfaces")

    for name in names:
        print(f"  - {name}")

connection.disconnect()
