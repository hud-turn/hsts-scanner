import nmap

target = "192.168.1.32"
port = "80"
script = "--script http-security-headers"
ns = nmap.PortScanner()
data = ns.scan(target, port,script)
print(data)