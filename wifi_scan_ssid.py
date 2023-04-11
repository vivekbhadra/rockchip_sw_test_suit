import subprocess as sp

def scan_and_find_ap():
    out = sp.run(['nmcli', '--mode', 'tabular', '-t', '--fields', 'SSID', 'device', 'wifi'], stdout=sp.PIPE)
    print(out.stdout.decode('utf-8'))

def main():
    scan_and_find_ap()

if __name__ == "__main__":
    main()
