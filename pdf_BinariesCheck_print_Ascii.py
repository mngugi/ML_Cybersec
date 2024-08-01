import PyPDF2
import sys

def check_pdf_for_binary_data(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Checking {num_pages} pages in {pdf_path} for binary data...")

            binary_pages = []

            for page_num in range(num_pages):
                page = reader.pages[page_num]
                raw_content = page.get_contents()
                
                if isinstance(raw_content, list):
                    raw_content = b''.join([part.get_data() for part in raw_content])
                else:
                    raw_content = raw_content.get_data()
                
                if is_binary(raw_content):
                    binary_pages.append(page_num + 1)
                    print(f"Binary data found on page {page_num + 1}.")

            if not binary_pages:
                print("No binary data found in the PDF.")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

def is_binary(data):
    # Heuristic method to detect binary data
    text_chars = bytearray({7, 8, 9, 10, 12, 13, 27}.union(set(range(0x20, 0x100)) - {0x7f}))
    return bool(data.translate(None, text_chars))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_pdf_binary.py <pdf_path>")
    else:
        pdf_path = sys.argv[1]
        check_pdf_for_binary_data("D34DM0053_Open_Letter_Mental_Health.pdf")

