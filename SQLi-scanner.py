import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

# intialize an HTTTP session and set the browser
s = requests.Session()
s.headers[
    "User-Agent"
] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"


def get_forms(url):
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")


def get_details(form):
    details = {}

    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs

    return details


def vulnerable(response):
    # a simple boolean function that determines whether a page is SQLi vulnerable from its response
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:

        if error in response.content.decode().lower():
            return True
        # no error detected
        return False


def scan_sqli(url):
    # test on URL
    for c in "\"'":
        # add quote/double quote character to the URL
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)
        # make the HTTP request
        res = s.get(new_url)
        if vulnerable(res):
            print("[+] SQL Injection vulnerability detected, link: ", new_url)
            return
    # test on HTML forms
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_details(form)
        for c in "\"'":
            # the data body we submit
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    # any input from that is hidden or has some value, use it in form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{c}"

            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "post":
                res = s.get(url, params=data)
            # test if the pgae is vulnerable
            if vulnerable(res):
                print("[+] SQL Injection vulnerability detected, linck: ", url)
                print("[+] Form: ")
                pprint(form_details)
                break


if __name__ == "__main__":
    url = ""  # put the URL of the site you want to scan here
    scan_sqli(url)
