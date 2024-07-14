# Kapil's Methodology

### Subdomain enumeration
```
python3 ~/BugHunting/new_scripts/subenumerator.py
```


### Host enumeration


```
httpx -l ./all.subs -p 80,443,8080,8443,8000,8008,8888,81,591,2080,2480,7474,5985,5986,1311,4711,5800,8081,9090,8181,8880,3000,3001,5000,5001,7000,7001,9091,9080,9443,10443,18080,28080,38080,48080 -t 200 -o httpx_status.hosts -status-code | awk '{print $1}' > httpx.hosts && cat all.subs| httprobe -c 40 | tee httprobe.hosts && cat httpx.hosts httprobe.hosts | sort -u | uniq | tee hosts.txt
```


### Port Scanning


```
naabu -list all.subs -c 50 -nmap-cli 'nmap -sV sC' -o naabu_scan.txt
```

### Screenshots 
```
gowitness file -f hosts/hosts.hosts -F --threads 16 
```

### Dir/file Discovery
```
dirsearch -l hosts.hosts -i 200,204,403,443 -x 500,502,429,501,503 -R 5 --random-agent -t 50 -w ~/BugHunting/new_scripts/wordlist.txt -o dirsearch.txt
```

### Endpoint/url Enumeration
```
katana -list hosts.hosts -passive -pss waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -f qurl -c 20 -o katana.txt && cat katana.txt | uro | tee urls.txt
```

### Wordpress enumeration

```
wpscan --url target.com --disable-tls-checks -e at -e ap -e u --enumerate ap --plugins-detection aggressive --force --api-token TOKEN
```
