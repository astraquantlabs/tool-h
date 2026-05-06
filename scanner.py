import nmap

def scan_network():
    nm = nmap.PortScanner()
    network_range = "192.168.1.0/24"

    nm.scan(hosts=network_range, arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        devices.append({
            "ip": host,
            "status": nm[host].state()
        })

    return devices