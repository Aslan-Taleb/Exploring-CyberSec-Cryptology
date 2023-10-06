import re

HTML_PAGE = 'grabbing/home.html'

# Updated regular expression pattern to allow for spaces and be case-insensitive
to_search = re.compile(r'<title>(.*)</title>', re.IGNORECASE)

with open(HTML_PAGE, 'r', encoding='utf-8') as file:  # Specify the encoding
    data = file.read()
    print("Contents of HTML file:")
    print(data)
    title_match = to_search.search(data)
    print("Title match object:")
    print(title_match)

    if title_match:
        title = title_match.group(1)
        print("Title:", title.strip())  # Strip leading and trailing whitespace
    else:
        print("Oh damn, there is no title.")
