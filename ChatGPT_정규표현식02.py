import re

# Regular expression for matching email addresses
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# List of example email addresses to test
emails = [
    'user1@example.com',
    'user2@example.co.uk',
    'user3@example.net',
    'user4@example.org',
    'user.5@example.com',
    'user-6@example.com',
    'user_7@example.com',
    'user+8@example.com',
    'user9@example.io',
    'user10@example.ai'
]

# Test each email address using the regular expression
for email in emails:
    match = re.search(email_regex, email)
    if match:
        print(f"Email address found: {match.group()}")
    else:
        print("Email address not found.")