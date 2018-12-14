# netgear_reboot
Reboot script for Netgear WNDR4500

I have a router that started failing after I filled up all 4 Ethernet ports, so this little script runs on a laptop connected via WiFi, and reboots the router every hour.

To set it up to run on boot, have a crontab something like this:

GECKODRIVER_PATH=/home/morphex/bin

@reboot /home/morphex/netgear_reboot/br.sh ROUTER_ADMIN_PASSWORD

