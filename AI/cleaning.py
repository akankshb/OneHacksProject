import re

def clean_text_keep_content(text: str) -> str:
    # 1. Remove obvious boilerplate lines (safe single-line deletes)
    line_remove_patterns = [
        r"^© ?\d{4}.*",              # copyright lines
        r"^Return to Table of Contents$", 
        r"^THIS PAGE IS INTENTIONALLY LEFT BLANK\.$", 
        r"^College Board.*$", 
        r"^Visit College Board.*$"
    ]
    for pattern in line_remove_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE|re.IGNORECASE)

    # 2. Normalize whitespace
    text = re.sub(r"\n{2,}", "\n", text)       # collapse multiple newlines
    text = re.sub(r"[ \t]+", " ", text)        # collapse multiple spaces/tabs
    text = re.sub(r" ?\n ?", "\n", text)       # clean spaces around newlines

    # 3. Ensure [D#] markers always start on a new line
    text = re.sub(r"(\[D\d+\])", r"\n\1", text)

    # 4. Shorten common long phrases (safe replacements)
    replacements = {
        "Advanced Placement Program": "AP",
        "multiple-choice": "MCQ",
        "free-response": "FRQ",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)

    # 5. Remove acknowledgments *names only*, not everything after
    text = re.sub(r"Acknowledgments\n.*?(?=\n[A-Z])", "Acknowledgments\n", text, flags=re.DOTALL)

    return text.strip()

# Example usage
with open("./data/APCHEM.txt", "r", encoding="utf-8", errors="ignore") as f:
    raw_text = f.read()

cleaned_text = clean_text_keep_content(raw_text)

# Save
with open("./data/APCHEM_courseguide_cleaned.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)
print(f"Original length: {len(raw_text)}")
print(f"Cleaned length: {len(cleaned_text)}")
print("Done. File saved.")
