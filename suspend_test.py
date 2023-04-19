#!/usr/bin/env python
import shlex
import datetime
import argparse
import subprocess as sp

def usage():
    print(":: Usage ::")
    print("\tpython suspend_test.py")

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def change_to_su():
    print("Inside change_to_su...")
    command_line = "sudo su"
    args = shlex.split(command_line)
    out = sp.call(args)

def suspend_and_wakeup(duration):
    print("Inside suspend_and_wakeup...")
    print("Suspension time set to " + str(duration))
    command_line = "sudo rtcwake -m no -l -s " + str(duration)
    args = shlex.split(command_line)
    print("Running rtcwake command...")
    out = sp.call(args) 
    command_line = "sudo systemctl suspend"
    args = shlex.split(command_line)
    print("Suspending at : " + get_time())
    print("Running suspend command...")
    out = sp.call(args)

def main():
    parser = argparse.ArgumentParser(description="Command line argument")
    parser.add_argument("-d", "--duration", default=300, help="Wakeup time in seconds.")
    options = parser.parse_args()
    suspend_and_wakeup(options.duration)

if __name__ == "__main__":
    main()