import argparse
import subprocess as sp

def speedtest():
    out = sp.run(['speedtest-cli'], stdout=sp.PIPE)
    print(out.stdout.decode('utf-8'))

def main():
    speedtest()

if __name__ == "__main__":
    main()

