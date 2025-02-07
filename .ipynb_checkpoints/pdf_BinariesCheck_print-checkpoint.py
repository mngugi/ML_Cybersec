import PyPDF2
import sys
import re

def is_binary_data(text):
    # Check for the presence of binary data in the text
    binary_regex = re.compile(r'[^\x09\x0A\x0D\x20-\x7E\x80-\xFF]')
    return binary_regex.search(text) is not None

def extract_binary_data(text):
    # Extract and return binary data found in the text
    binary_regex = re.compile(r'[^\x09\x0A\x0D\x20-\x7E\x80-\xFF]')
    return binary_regex.findall(text)

def check_pdf_for_binary_data(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Checking {num_pages} pages in {pdf_path} for binary data...")

            binary_pages = []

            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                if text and is_binary_data(text):
                    binary_pages.append(page_num + 1)
                    binary_data = extract_binary_data(text)
                    print(f"Binary data found on page {page_num + 1}:")
                    print(binary_data)

            if not binary_pages:
                print("No binary data found in the PDF.")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_pdf_binary.py <pdf_path>")
    else:
        pdf_path = sys.argv[1]
        check_pdf_for_binary_data("D34DM0053_Open_Letter_Mental_Health.pdf")

