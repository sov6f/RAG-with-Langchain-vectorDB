from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env variables
load_dotenv()

try:
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    # Test call
    response = llm.invoke("Say 'Gemini is working!'")

    print("✅ Gemini Response:")
    print(response.content)

except Exception as e:
    print("❌ Gemini is not responding")
    print(f"Error: {e}")


# llm1 = ChatGroq(
#     model="qwen/qwen3-32b",
#     temperature=0
# )