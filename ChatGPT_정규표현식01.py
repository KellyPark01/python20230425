import re

# create a regular expression pattern for matching email addresses
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# test string containing an email address
test_string = "My email is john.doe@example.com, please email me there."

# search for the first email address in the test string
match = email_regex.search(test_string)

if match:
    print("Email address found:", match.group())
else:
    print("No email address found.")