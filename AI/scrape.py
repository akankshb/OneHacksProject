from pathlib import Path
import pdfplumber

# Get absolute path to the ApChem folder
base_dir = Path(__file__).resolve().parent.parent  # up from AI/ to OneHacksProject/
root_dir = base_dir / "ApMaterial" / "ApChem"
print("Looking in:", root_dir)
f = open("data/APCHEM.txt", "w")
f.write("System:\nYou're tasks are to create full length AP Chemistry tests or short tests for a specific topic, similar to the documents that have been provided. Only past AP FRQs and the course description have been provided; therefore, you will need to create the MCQ section yourself: 60 MCQ and 7 FRQ for full AP tests. Only create questions that test the topics provided in the document.\n")
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