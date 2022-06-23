import requests

# the domain to scan for subdomains
domain = "DOMAIN.COM"  # domain you want to scan

# read all subdomains
file = open(
    "YOUR FILE.text"
)  # save the subdomains you want https://github.com/rbsec/dnscan into a file
content = file.read()
subdomains = content.splitlines()

# The list of discovered subdomains
discovered_subdomains = []
for subdomain in subdomains:
    # construct the URL
    url = f"http://{subdomain}.{domain}"
    try:
        # this error raise when the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # print nothing if the subdomain does not exist
        pass
    else:
        print("[+]", url)
        discovered_subdomains.append(url)
    # save the discovered subdomains into a file
    with open("discovered_subdomains.txt", "w") as f:
        print(subdomain, file=f)
