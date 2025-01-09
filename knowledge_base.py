import pdfplumber


knowledge_base = ""
# Open the PDF file
with pdfplumber.open("whitepaper.pdf") as pdf:
    for page in pdf.pages:
        # print(page.extract_text())
        knowledge_base += page.extract_text()

print(knowledge_base)