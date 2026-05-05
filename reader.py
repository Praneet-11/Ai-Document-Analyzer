from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    
    return full_text

filename = "research.pdf" 
print(f"Reading {filename}...")

try:
    content = extract_text_from_pdf(filename)
    print("\n--- FIRST 500 CHARACTERS OF PDF ---")
    print(content[:500])
except Exception as e:
    print(f"Error: {e}. Make sure the filename matches!")