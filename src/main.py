from dotenv import load_dotenv
import os

load_dotenv()
def main():
    print(f"API Key {os.getenv('OPENAI_API_KEY')}")
    



if __name__ == "__main__":
    main()
    
