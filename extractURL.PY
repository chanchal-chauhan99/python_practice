import re

text = "Check out the Visit https://www.example.com and http://another-example.org and https://website.com for more info."

url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

urls = re.findall(url_pattern, text)

print(', '.join(urls))