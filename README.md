# netgear_reboot
Reboot script for Netgear WNDR4500

I have a router that started failing after I filled up all 4 Ethernet ports,
even after updating firmware, so this little script runs on a laptop
connected via WiFi, and reboots the router every hour.

To set it up to run on boot, have a crontab something like this:

START CRONTAB
HOME=/home/morphex

@reboot /home/morphex/netgear_reboot/br.sh ROUTER_ADMIN_PASSWORD
END CRONTAB

Where HOME is the home directory of the user, where netgear_reboot is the
directory for this script, and bin is the directory which contains
geckodriver, which can be downloaded from here:

https://github.com/mozilla/geckodriver/releases

Also, on my laptop, the network routing gets screwed up, so I have to allow
my user morphex to run sudo on the command to reset the routing table:

morphex ALL=(ALL) NOPASSWD: /sbin/ip route del 0/0

the above line is added to /etc/sudoers
