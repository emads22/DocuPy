import io
import sys
import subprocess
from transformers import AutoTokenizer
from app_config import *

# =============================={ Tab Functions }==============================

def stream_gpt(system_prompt, user_prompt):
    stream = gpt.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        stream=True)
    reply = ""
    for chunk in stream:
        reply += chunk.choices[0].delta.content or ""
        yield reply.replace("```python\n", "").replace("```cpp\n", "").replace("```", "")

def stream_claude(system_prompt, user_prompt):
    response = claude.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    reply = ""
    with response as stream:
        for text in stream.text_stream:
            reply += text
            yield reply.replace("```python\n", "").replace("```cpp\n", "").replace("```", "")

def stream_gemini(system_prompt, user_prompt):
    gemini = google_genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=system_prompt
    )
    stream = gemini.generate_content(
        contents=user_prompt,
        stream=True
    )
    reply = ""
    for chunk in stream:
        reply += chunk.text or ""
        yield reply.replace("```python\n", "").replace("```cpp\n", "").replace("```", "")

def stream_code_qwen(system_prompt, user_prompt):
    tokenizer = AutoTokenizer.from_pretrained(CODE_QWEN_MODEL)
    model_input = tokenizer.apply_chat_template(
        conversation=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        tokenize=False,
        add_generation_prompt=True
    )
    stream = code_qwen.text_generation(
        prompt=model_input,
        stream=True,
        details=True,
        max_new_tokens=MAX_TOKENS
    )
    reply = ""
    for chunk in stream:
        reply += chunk.token.text or ""
        yield reply.replace("```python\n", "").replace("```cpp\n", "").replace("```", "")

def set_prompts(user_input, action):
    action = action.lower()

    if action == ACTION_A.lower():
        system_prompt = SYSTEM_PROMPT_COMMENTS
        user_prompt = user_prompt_comments(user_input)
    elif action == ACTION_B.lower():
        system_prompt = SYSTEM_PROMPT_TESTS
        user_prompt = user_prompt_tests(user_input)
    elif action == ACTION_C.lower():
        system_prompt = SYSTEM_PROMPT_CONVERT
        user_prompt = user_prompt_convert(user_input)
    else:
        return None, None
    
    return system_prompt, user_prompt

def stream_response(user_input, model, action):
    system_prompt, user_prompt = set_prompts(user_input, action)
    if not all((system_prompt, user_prompt)):
        raise ValueError("Unknown Action")

    match model:
        case "GPT":
            yield from stream_gpt(system_prompt, user_prompt)

        case "Claude":
            yield from stream_claude(system_prompt, user_prompt)

        case "Gemini":
            yield from stream_gemini(system_prompt, user_prompt)

        case "CodeQwen":
            yield from stream_code_qwen(system_prompt, user_prompt)

def generate_comments(python_code, selected_model):
    for model in MODELS_IN_USE:
        if model == selected_model:
            yield from stream_response(python_code, model, action=ACTION_A)
            return  # Exit the function immediately after exhausting the generator
    raise ValueError("Unknown Model")

def generate_tests(python_code, selected_model):
    for model in MODELS_IN_USE:
        if model == selected_model:
            yield from stream_response(python_code, model, action=ACTION_B)
            return  # Exit the function immediately after exhausting the generator
    raise ValueError("Unknown Model")

def convert_code(python_code, selected_model):
    for model in MODELS_IN_USE:
        if model == selected_model:
            yield from stream_response(python_code, model, action=ACTION_C)
            return  # Exit the function immediately after exhausting the generator
    raise ValueError("Unknown Model")

# =============================={ Running Code Functions }==============================

def run_python_exec(code):
    try:
        # Capture stdout using StringIO
        output = io.StringIO()

        # Redirect stdout to StringIO
        sys.stdout = output

        # Execute the provided Python code
        exec(code)
    finally:
        # Restore original stdout
        sys.stdout = sys.__stdout__

    # Return the captured output
    return output.getvalue()

# Improved running python function
def run_python(code):
    # Save the Python code to a file
    with open(TEMP_DIR / "python_code.py", "w") as python_file:
        python_file.write(code)

    try:
        # Execute the Python code
        result = subprocess.run(
            ["python", str(TEMP_DIR / "python_code.py")],
            check=True, text=True, capture_output=True
        )

        # Return the program's output
        return result.stdout

    except subprocess.CalledProcessError as e:
        # Handle compilation or execution errors
        return f"An error occurred during execution:\n{e.stderr}"

    finally:
        # Clean up: Delete the Python code file and executable
        file_path = TEMP_DIR / "python_code.py"
        if file_path.exists():
            file_path.unlink()

def run_cpp(code):
    # Save the C++ code to a file
    with open(TEMP_DIR / "cpp_code.cpp", "w") as cpp_file:
        cpp_file.write(code)

    try:
        # Compile the C++ code
        subprocess.run(
            ["g++", "-o", str(TEMP_DIR / "cpp_code"), str(TEMP_DIR / "cpp_code.cpp")],
            check=True, text=True, capture_output=True
        )

        # Execute the compiled program
        result = subprocess.run(
            [str(TEMP_DIR / "cpp_code")],
            check=True, text=True, capture_output=True
        )

        # Return the program's output
        return result.stdout

    except subprocess.CalledProcessError as e:
        # Handle compilation or execution errors
        error_context = "during compilation" if "cpp_code.cpp" in e.stderr else "during execution"
        return f"An error occurred {error_context}:\n{e.stderr}"

    finally:
        # Clean up: Delete the C++ source file and executable
        for filename in ["cpp_code.cpp", "cpp_code", "cpp_code.exe"]:
            file_path = TEMP_DIR / filename
            if file_path.exists():
                file_path.unlink()
