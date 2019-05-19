
# Resources
- List of tools: https://www.elmelectronics.com/help/obd/software/#Linux
- This original repo: https://github.com/roflson/pyobd


#Cookbook
```sh
# Copy dir local to remote
rsync -ra /home/andrew/Workspace/pyobd pi@192.168.8.119:/home/pi/

# Install screen drivers
wget http://www.4dsystems.com.au/downloads/4DPi/All/4d-hats_4-4-34_v1.1.tar.gz
sudo tar -xzvf 4d-hats_4-4-34_v1.1.tar.gz -C /

## SSH issue: Connection reset port 22
sudo rm /etc/ssh/ssh_host_*
sudo dpkg-reconfigure openssh-server
```