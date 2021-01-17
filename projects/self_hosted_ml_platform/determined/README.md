```bash
nmcli dev show wlp7s0
```

```bash
iptables -t nat -I PREROUTING -p tcp -d 192.168.0.101/24 --dport 8080 -j DNAT --to-destination 127.0.0.1:8080
sudo sysctl -w net.ipv4.conf.wlp7s0.route_localnet=1
```
