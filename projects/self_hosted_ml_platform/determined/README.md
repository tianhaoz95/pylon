# Determined Setup

```bash
nmcli dev show wlp7s0
```

> Check [here](https://askubuntu.com/questions/197628/how-do-i-find-my-network-ip-address-netmask-and-gateway-info) for the original answer.

```bash
iptables -t nat -I PREROUTING -p tcp -d 192.168.0.101/24 --dport 8080 -j DNAT --to-destination 127.0.0.1:8080
sudo sysctl -w net.ipv4.conf.wlp7s0.route_localnet=1
```

> Check [here](https://unix.stackexchange.com/questions/111433/iptables-redirect-outside-requests-to-127-0-0-1) for the original answer.
