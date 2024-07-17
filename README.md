# Kapil's Methodology

### Subdomain enumeration
```
python3 ~/BugHunting/new_scripts/subenumerator.py
```

### Subdomain Takeover
```
subzy run --targets unique_subdomains.txt --concurrency 100 --hide_fails --verify_ssl
```

### Host enumeration


```
httpx -l ./unique_subdomains.txt -p 80,443,8080,8443,8000,8008,8888,81,591,2080,2480,7474,5985,5986,1311,4711,5800,8081,9090,8181,8880,3000,3001,5000,5001,7000,7001,9091,9080,9443,10443,18080,28080,38080,48080 -t 200 -o httpx_status.hosts -status-code | awk '{print $1}' > httpx.hosts && cat ./unique_subdomains.txt| httprobe -c 40 | tee httprobe.hosts && cat httpx.hosts httprobe.hosts | sort -u | uniq | tee hosts.txt
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
katana -list hosts.txt -passive -pss waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -f qurl,ufile -c 20 -o katana.txt && cat katana.txt | uro | tee urls.txt
```

### js secrets
```
cat urls.txt| grep ".js$" | while read url; do python3 /opt/SecretFinder/SecretFinder.py -i $url -o cli |tee js_secrets.txt; done
```

### Google Dorking
```
Hunt for sensitive informatin on all search enginers
google : https://pentest-tools.com/information-gathering/google-hacking
bing
duckduckgo
yahoo
shodan
censys
OSINT
Github
S3 Bucket Enumeration
```

### Wordpress enumeration

```
wpscan --url target.com --rua -t 50 --disable-tls-checks -e vp,vt,cb,u,dbe --plugins-detection aggressive --api-token TOKEN
```

### Xss Automation
```
cat urls.txt| gf xss | Gxss -p Kapilxss | dalfox pipe
```
### SQLi Automation
```
cat urls.txt | urldedupe | gf sqli > sql.urls && sqlmap -m sql.urls --batch --dbs --risk 3 --level 5 --random-agent | tee -a sqli.log
```
### Open redirect Automation
```

```
### Manul Testing
After this much autoomation i think now is time to go for manual testing
Fire your burp and get started
```
```

## Tools used
```
subfinder
assetfinder
sublist3r
certsh.py
subzy
httpx
httprobe
naabu
nmap
gowitness
dirsearch
katana
uro
wpscan
Gxss
urldedupe
dalfox
```


### Burp Setup

#### Extensions
```
autoriser
param miner
```
#### Confiurations
```
Use match and replace
```
