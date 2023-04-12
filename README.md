Copy these scripts in a USB stick and attach it in the board (I am doing it in Rock 4C+, it will work for all other platforms).  
On the board, copy the scripts from the USB to the home folder (or any other folder or your choice). To achieve that follow the below steps:  
~$ lsblk  
~$ udisksctl mount -b /dev/sda1  
This should show you where it is mounting the USB drive, a message on the console somewhat like below:  
Mounted /dev/sda1 at /media/radxa/BB63-6ED4  
~$ cp /media/radxa/BB63-6ED4/*.py .  
Now you are ready to run the scripts to do the following:  
Search available wifi access points (AP):   
~$ python wifi_scan_ssid.py  
        b. The above will search and display the available SSIDs in your test setup/home. Choose the one you would like to connect to in the below command:  
           ~$ python wifi_connect_ssid.py -s <SSID to connect to>  
            You will be prompted to type in the default password for the build, and then it will ask the password for the SSID. Please type these in and the script
            should successfully connect you to the SSID you specified in the command line.   
       4. Now one you have successfully executed the above, please run the following command:  
            ~$ source customize_environment.sh  
       5. Speed Test:  
            ~$ python wifi_test_speed_simple.py  
            ~$ python wifi_test_speed_full.py  

I have tested the above in Rock 4C+. I will test it on Rock 5B as well very soon.  
