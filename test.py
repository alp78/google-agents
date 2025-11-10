from google import genai
import os

# Check if the environment variable is set
if "GEMINI_API_KEY" not in os.environ:
    print("Error: GEMINI_API_KEY environment variable not set.")
else:
    try:
        # 1. Initialize the client
        #    It automatically finds the 'GEMINI_API_KEY'
        client = genai.Client()

        # 2. Generate content directly
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents="Hello, how does Gemini 2.5 Pro work?"
        )
        
        # 3. Print the text
        print(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your API key and model name ('gemini-2.5-pro').")