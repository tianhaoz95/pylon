# Notes

## 2021-02-28

* Instruction for setting up Chrome Remote Desktop on Linux: [instructions](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DDesktop&hl=en#zippy=%2Cuse-chrome-remote-desktop-on-linux)
* How to reconfigure between lightgdm and gdm3: https://askubuntu.com/questions/152256/how-do-i-switch-from-lightdm-to-gdm
* Wake on LAN usually use port 7 or 9 according to https://en.wikipedia.org/wiki/Wake-on-LAN
* To edit grub config, change the content in `/etc/defaut/grub`, check https://www.gnu.org/software/grub/manual/grub/grub.html for config options.
* To find the correct interface name for WoL, use `arp -n` and the `Iface` will be the interface to specify in `etherwake` command.

```bash
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.0.167            ether   04:d9:f5:f3:ca:91   C                     wlo1
192.168.0.1              ether   98:da:c4:8e:a2:85   C                     wlo1
192.168.0.117            ether   1c:f2:9a:66:1c:d9   C                     wlo1
```

* To wake a machine locally with `etherwake`, use `sudo etherwake -i wlo1 04:d9:f5:f3:ca:91` where the `i` is the interface name and the number is the MAC address.
* To enable WoL on bootup, see https://www.techrepublic.com/article/how-to-enable-wake-on-lan-in-ubuntu-server-18-04/
* Ubuntu official docs on setting up WoL: https://help.ubuntu.com/community/WakeOnLan
* Setting up router port forwarding for WoL (for TP-Link, go to NAT Forwarding -> Virtual Servers):

![TP link setup](/asset/screenshot_setup_router_port_forwarding_for_wol.png)

![WoL from teamviewer](/asset/screenshot_wol_from_teamviewer_site.png)

* To find out the public ip address, do `curl ifconfig.me`.