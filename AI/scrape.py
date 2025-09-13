from pathlib import Path
import pdfplumber

# Get absolute path to the ApChem folder
base_dir = Path(__file__).resolve().parent.parent  # up from AI/ to OneHacksProject/
root_dir = base_dir / "ApMaterial" / "ApChem"
print("Looking in:", root_dir)
f = open("data/APCHEM.txt", "w")
f.write("System:\nYou are an AP Chemistry help bot; based on the user’s request, generate either guided notes, a study guide, or a practice test; always stay within AP Chemistry content only, follow the specified topic(s) and requested length, and if creating a test use the format specified in the request: for MCQ write multiple-choice questions with 4 options (A–D) plus the correct answer, for FRQ write free-response questions with clear prompts and sample answers. Give the questions first, then underneath in a new section give the answer key. Avoid special characters. ONLY FOLLOW THE DIRECTIONS!\n")
if not root_dir.exists():
    print("Directory not found:", root_dir)
else:
    # Loop through all PDFs recursively
    n=1
    for file in root_dir.rglob("*.pdf"):
        print("📄 Processing:", file)

        try:
            temp = f"[D{n}]: "
            if "sg" in str(file):
                temp += "Scoring Guide "
            elif "frq" in str(file):
                temp+= "Free Response "
            else:
                temp += "Course Description \n"
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:  # avoid None
                        temp += page_text + "\n"

            # Save extracted text next to the PDF
            f.write(temp)
        except Exception as e:
            print("Could not process", file, "->", e)
        n+=1
f.close()
print("File succesfully closed")