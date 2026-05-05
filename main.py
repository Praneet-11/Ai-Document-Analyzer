from pypdf import PdfReader
from google import genai

# 1. SETUP
YOUR_API_KEY = "AIzaSyAt18bWisPez_DvupupeCV1gPljSq8iyAU"
client = genai.Client(api_key=YOUR_API_KEY)

def analyze_document(pdf_path):
    # 2. READ THE PDF
    print(f"Reading {pdf_path}...")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # 3. SEND TO AI
    print("Asking Gemini to analyze...")
    prompt = f"You are an expert researcher. Based on this text, explain the 'Proof-of-Authority' mechanism mentioned in 2 simple sentences: \n\n{text}"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"API Still Locked. Error: {e}"

# RUN IT
filename = "research.pdf" # Make sure this matches your file!
result = analyze_document(filename)

print("\n--- GEMINI'S ANALYSIS ---")
print(result)