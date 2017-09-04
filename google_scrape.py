from urllib.parse import urlencode, urlparse, parse_qs

from lxml.html import fromstring
from requests import get

keyword = input("Enter your keyword: ")

standard_url = "https://www.google.com/search?q={}".format(keyword)
gov_url = "https://www.google.com/search?q={}+site%3A.gov".format(keyword)
edu_url = "https://www.google.com/search?q={}+site%3A.edu".format(keyword)
org_url = "https://www.google.com/search?q={}+site%3A.org".format(keyword)
wsj_url = "https://www.google.com/search?q={}+site%3Awsj.com".format(keyword)
nyt_url = "https://www.google.com/search?q={}+site%3Anytimes.com".format(keyword)
forbes_url = "https://www.google.com/search?q={}+site%3Aforbes.com".format(keyword)

# Scrape url for government sites
gov_raw = get(gov_url).text
gov_page = fromstring(gov_raw)

print("\nGOV Pages")
for result in gov_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

# Scrape url for edu sites
edu_raw = get(edu_url).text
edu_page = fromstring(edu_raw)

print("\nEDU Pages")
for result in edu_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

# Org standard sites
org_raw = get(org_url).text
org_page = fromstring(org_raw)

print("\nORG Pages")
for result in org_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

# Scrape standard sites
standard_raw = get(standard_url).text
standard_page = fromstring(standard_raw)

print("\nStandard Pages")
for result in standard_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

# Scrape WSJ sites
wsj_raw = get(wsj_url).text
wsj_page = fromstring(wsj_raw)

print("\nWSJ Pages")
for result in wsj_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

# Scrape NYT sites
nyt_raw = get(nyt_url).text
nyt_page = fromstring(nyt_raw)

print("\nNYT Pages")
for result in nyt_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

# Scrape Forbes sites
forbes_raw = get(forbes_url).text
forbes_page = fromstring(forbes_raw)

print("\nForbes Pages")
for result in forbes_page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    print(url[0])

