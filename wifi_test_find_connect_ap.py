import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="Command line argument")
parser.add_argument("-s", "--ssid", default="dummy", help="SSID to connect")
parser.add_argument("-p", "--password", default="1234567", help="Password to connect to SSID")
options = parser.parse_args()

def scan_and_find_ap():
    out = sp.run(['nmcli', '--mode', 'tabular', '-t', '--fields', 'SSID', 'device', 'wifi'], stdout=sp.PIPE)
    ap_list = out.stdout.decode('utf-8').split('\n')
    for ap in ap_list:
        if ap == options.ssid:
            print("SSID found in scan.")
            found = True
            break
    if found != True:
        print("SSID not found in scan")
    return ap

def connect_ssid(ap, pass_word):
    out = sp.run(['sudo', 'nmcli', 'dev', 'wifi', 'connect', ap, 'password', pass_word])

def main():
    parser = argparse.ArgumentParser(description="Command line argument")
    parser.add_argument("-s", "--ssid", default="dummy", help="SSID to connect")
    parser.add_argument("-p", "--password", default="1234567", help="Password to connect to SSID")
    options = parser.parse_args()

    ap = scan_and_find_ap()
    connect_ssid(ap, options.password)


if __name__ == "__main__":
    main()

