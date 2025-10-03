import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Test OpenAI
def test_openai():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Say 'API works!'"}],
            max_tokens=10
        )
        print("✓ OpenAI API works!")
        print(f"Response: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"✗ OpenAI API failed: {e}")
        return False

# Test Perplexity (if you have access)
def test_perplexity():
    import httpx
    api_key = os.getenv("PERPLEXITY_API_KEY")
    
    if not api_key:
        print("⚠ No Perplexity API key found - skipping")
        return True
    
    try:
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [{"role": "user", "content": "test"}]
        }
        
        response = httpx.post(url, json=data, headers=headers, timeout=30)
        if response.status_code == 200:
            print("✓ Perplexity API works!")
            return True
        else:
            print(f"✗ Perplexity API failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Perplexity API failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing APIs...\n")
    test_openai()
    print()
    test_perplexity()