import re

def clean_text(raw_text: str) -> str:
# Insert double newline before [D####] + keep title on same line
    # Look for [D####] followed by text (the title) until the next [D or end of text
    text = re.sub(r'\[D\d+\]\s*[^[]+', lambda m: '\n\n' + m.group(0).strip() + '\n', raw_text)

    # Normalize spaces **without removing newlines**
    text = re.sub(r'[ \t]+', ' ', text)  # compress spaces/tabs


    # Remove common legal boilerplate phrases
    boilerplate_patterns = [
        r"all rights reserved.*",
        r"no part of this publication.*",
        r"this material is provided.*",
        r"without warranty of any kind.*",
        r"disclaimer.*",
        r"reproduced, stored in.*",
        r"permission of the publisher.*",
        r"printed in [A-Za-z]+.*",
        r"© 2025 College Board.",
        r"Visit College Board on the web: collegeboard.org"
    ]

    for pattern in boilerplate_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Clean up extra spaces/newlines
    text = re.sub(r'\n\s*\n+', '\n\n', text)  # normalize paragraph breaks
    text = re.sub(r' +', ' ', text).strip()

    return text


with open("data/APCHEM.txt", 'r') as f:
    text = f.read()
    text = clean_text(text)
    f.close()

with open("data/APCHEM.txt", 'w') as f:
    f.write(text)
    f.close()
