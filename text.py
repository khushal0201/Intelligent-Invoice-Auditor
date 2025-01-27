import re

# Your raw HTML content
with open('result_data.txt', 'r') as file:
    html_content = file.read()

# Use regular expression to find all <tr> blocks
tr_elements = re.findall(r'<tr.*?>(.*?)</tr>', html_content, re.DOTALL)

# Wrap the <tr> tags back around the captured content
tr_elements = ['<tr>' + tr + '</tr>' for tr in tr_elements]

# Display the array of strings
for item in tr_elements:
    print(item)
    print("---------------")
