from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# Load .env variables
load_dotenv()

llm1 = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0
)

response = llm1.invoke("Say 'groq is working!'")

print("✅ Groq Response:")
print(response.content)

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Test call
response = llm.invoke("Say 'Gemini is working!'")

print("✅ Gemini Response:")
print(response.content)

