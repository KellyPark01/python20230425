import re

# Regular expression for matching Korean social security numbers
ssn_regex = r'\d{6}-\d{7}'

# List of example social security numbers to test
ssns = [
    '800101-1234567',
    '810202-2345678',
    '820303-3456789',
    '830404-4567890',
    '840505-5678901',
    '850606-6789012',
    '860707-7890123',
    '870808-8901234',
    '880909-9012345',
    '890101-0123456'
]

# Test each social security number using the regular expression
for ssn in ssns:
    match = re.search(ssn_regex, ssn)
    if match:
        print(f"Valid social security number: {match.group()}")
    else:
        print("Invalid social security number.")
