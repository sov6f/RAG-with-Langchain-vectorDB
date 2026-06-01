import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import (TextLoader)


from dotenv import load_dotenv

load_dotenv()

def load_text_file():
    #create a temporary text file for testing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name

    try:
        #load the text file using TextLoader
        loader = TextLoader(temp_file_path)
        documents = loader.load()


        print(f"Loaded {len(documents)} document(s)")
        print(f"Content Preview: {documents[0].page_content[:100]}...")
        print(f"Metadata: {documents[0].metadata}")
        
        #print the content of the loaded documents
        # for doc in documents:
        #     print("Document Content:")
        #     print(doc)
        #     print(doc.page_content)
    finally:
        #clean up the temporary file
        os.remove(temp_file_path)

if __name__ == "__main__":
    load_text_file()