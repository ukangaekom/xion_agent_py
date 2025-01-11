import pdfplumber


knowledge = ""
# Open the PDF file
with pdfplumber.open("whitepaper.pdf") as pdf:
    for page in pdf.pages:
        # print(page.extract_text())
        knowledge += page.extract_text()



if __name__ == "__main__":
    pass