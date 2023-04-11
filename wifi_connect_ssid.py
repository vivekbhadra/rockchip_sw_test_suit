import argparse
import subprocess as sp

def usage():
    print(":: Usage ::")
    print("\tpython wifi_test_find_ap.py -s <SSID> -p <password>")

def scan_and_find_ap(ssid):
    out = sp.run(['nmcli', '--mode', 'tabular', '-t', '--fields', 'SSID', 'device', 'wifi'], stdout=sp.PIPE)
    ap_list = out.stdout.decode('utf-8').split('\n')
    found = False
    for ap in ap_list:
        if ap == ssid:
            print("SSID found in scan.")
            found = True
            break
    if found != True:
        print("SSID not found in scan, make sure you have provided a valid SSID.")
        usage()
    else:
        print("SSID found in scan")
 
    return ap

def connect_ssid(ap, pass_word='xyz'):
    out = sp.run(['sudo', 'nmcli', '--ask', 'dev', 'wifi', 'connect', ap])

def show_active_con():
    out = sp.run(['nmcli', 'connection', 'show', '--active'], stdout=sp.PIPE)


def main():
    parser = argparse.ArgumentParser(description="Command line argument")
    parser.add_argument("-s", "--ssid", default="dummy", required=True, help="SSID to connect")
    options = parser.parse_args()

    ap = scan_and_find_ap(options.ssid)
    if ap:
        connect_ssid(ap)
        show_active_con()

if __name__ == "__main__":
    main()

