from urllib.request import urlopen

#Connect to the website:
url = "https://docs.python.org/2/library/json.html"
conn = urlopen(url)

# Download data:
raw_data = conn.read()
page_content = raw_data.decode("utf8")

print(page_content)