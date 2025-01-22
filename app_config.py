import os
import openai
import anthropic
import google.generativeai as google_genai
from huggingface_hub import login, InferenceClient
from dotenv import load_dotenv
from pathlib import Path

# Load the .env file
load_dotenv()

# Log in to Hugging Face using the token and add it to git credentials
hf_token = os.getenv('HF_TOKEN')
login(token=hf_token, add_to_git_credential=True)

# Endpoint URL for accessing the Code Qwen model through Hugging Face
CODE_QWEN_URL = os.getenv('CODE_QWEN_URL')

# Initialize inference clients with every model using API keys
gpt = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
claude = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
google_genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
code_qwen = InferenceClient(CODE_QWEN_URL, token=hf_token)

# =============================={ Models and other constants }==============================

OPENAI_MODEL = "gpt-4o"
CLAUDE_MODEL = "claude-3-5-sonnet-20240620"
GEMINI_MODEL = "gemini-1.5-pro"
CODE_QWEN_MODEL = "Qwen/CodeQwen1.5-7B-Chat"

MODELS_IN_USE = ["GPT", "Claude", "Gemini", "CodeQwen"]

MAX_TOKENS = 2000

ACTION_A = "commenting"
ACTION_B = "testing"
ACTION_C = "converting"

# Define and create the path for the "temp_files" directory within the current script's directory
TEMP_DIR = Path.cwd() / "temp_files"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# =============================={ Predefined Python scripts }==============================

PYTHON_SCRIPT_EASY = """
import time

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    start_time = time.time()
    text = "Hello, World!"
    print(f"- Original string: {text}")
    print("- Reversed string:", reverse_string(text))
    execution_time = time.time() - start_time  
    print(f"\\n=> Execution Time: {execution_time:.6f} seconds")
"""

PYTHON_SCRIPT_INTERMEDIATE = """
import time

def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]

if __name__ == "__main__":
    start_time = time.time()
    text = "Racecar"
    if is_palindrome(text):
        print(f"- '{text}' is a palindrome!")
    else:
        print(f"- '{text}' is Not a palindrome.")
    execution_time = time.time() - start_time  
    print(f"\\n=> Execution Time: {execution_time:.6f} seconds")
"""

PYTHON_SCRIPT_HARD = """
import time

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

if __name__ == "__main__":
    start_time = time.time()
    n = 20
    print(f"- Generating primes up to: {n}")
    print("- Prime numbers:", generate_primes(n))
    execution_time = time.time() - start_time  
    print(f"\\n=> Execution Time: {execution_time:.6f} seconds")
"""

PYTHON_SCRIPTS = {
    "reverse_string" : PYTHON_SCRIPT_EASY,
    "is_palindrome" : PYTHON_SCRIPT_INTERMEDIATE,
    "generate_primes" : PYTHON_SCRIPT_HARD,
    "custom" : """
# Write your custom Python script here
if __name__ == "__main__":
    print("Hello, World!")
"""
}

# =============================={ Relative system prompts }==============================

SYSTEM_PROMPT_COMMENTS = """
You are an AI model specializing in enhancing Python code documentation.
Generate detailed and precise docstrings and inline comments for the provided Python code.
Ensure the docstrings clearly describe the purpose, parameters, and return values of each function.
Inline comments should explain complex or non-obvious code segments.
Do not include any introductions, explanations, conclusions, or additional context.
Return only the updated Python code enclosed within ```python ... ``` for proper formatting and syntax highlighting.
"""

SYSTEM_PROMPT_TESTS = """
You are an AI model specializing in generating comprehensive unit tests for Python code.
Create Python unit tests that thoroughly validate the functionality of the given code.
Use the `unittest` framework and ensure edge cases and error conditions are tested.
Do not include any comments, introductions, explanations, conclusions, or additional context.
Return only the unit test code enclosed within ```python ... ``` for proper formatting and syntax highlighting.
"""

SYSTEM_PROMPT_CONVERT = """
You are an AI model specializing in high-performance code translation.
Translate the given Python code into equivalent, optimized C++ code.
Focus on:
- Using efficient data structures and algorithms.
- Avoiding unnecessary memory allocations and computational overhead.
- Ensuring minimal risk of integer overflow by using appropriate data types.
- Leveraging the C++ Standard Library (e.g., `<vector>`, `<algorithm>`) for performance and readability.
Produce concise and efficient C++ code that matches the functionality of the original Python code.
Do not include any comments, introductions, explanations, conclusions, or additional context..
Return only the C++ code enclosed within ```cpp ... ``` for proper formatting and syntax highlighting.
"""

# =============================={ Relative user prompts }==============================

def user_prompt_comments(python_code):
    user_prompt = f"""
Add detailed docstrings and inline comments to the following Python code:

```python
{python_code}
```
"""
    return user_prompt


def user_prompt_tests(python_code):
    user_prompt = f"""
Generate unit tests for the following Python code using the `unittest` framework:

```python
{python_code}
```
"""
    return user_prompt


def user_prompt_convert(python_code):
    user_prompt = f"""
Convert the following Python code into C++:

```python
{python_code}
``` 
"""
    return user_prompt
