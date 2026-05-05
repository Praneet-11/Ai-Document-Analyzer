from google import genai
import time

# Use the NEW key you generated (the secret one!)
YOUR_API_KEY = "PASTE_YOUR_NEW_SECRET_KEY_HERE"

client = genai.Client(api_key=YOUR_API_KEY)

print("Attempting to bypass quota jail...")

try:
    response = client.models.generate_content(
        model='gemini-1.5-flash-latest', 
        contents='Describe a Royal Enfield Bullet 350 in one word.'
    )
    print("\n--- IT WORKED! ---")
    print(response.text)
except Exception as e:
    print("\n--- STILL LOCKED OUT ---")
    print(f"Error: {e}")
    print("\nDon't worry, Praneet. If this fails, we switch to the AI Studio Sandbox.")