import gradio as gr
from app_tools import *

# =============================={ Gradio UI Tabs Functions }==============================

# Tab to Document Code with Docstrings and Comments
def docs_comments_ui():
    with gr.Tab("Docstrings & Comments"):
        gr.Markdown("""
        ## Document Code with Docstrings and Comments
        This tab allows you to automatically generate docstrings and inline comments for your Python code.
        - Paste your Python code into the **`Python Code`** textbox.
        - Select your preferred model (GPT, Claude, Gemini, or CodeQwen) to process the code.
        - Click the **`Add Docstrings & Comments`** button to generate well-documented Python code.
        The generated code will appear in the **`Python Code with Docstrings and Comments`** textarea.
        """)
        with gr.Row():
            python = gr.Textbox(label="Python Code:", lines=20,
                                value=PYTHON_SCRIPTS["custom"], elem_classes=["python"])
            python_with_comments = gr.TextArea(
                label="Python Code with Docstrings and Comments:", interactive=True, lines=20, elem_classes=["python"])
        with gr.Row():
            python_script = gr.Dropdown(choices=list(PYTHON_SCRIPTS.keys(
            )), label="Select a Python script", value="custom", elem_classes=["model"])
            comments_btn = gr.Button(
                "Add Docstrings & Comments", elem_classes=["button"])
            model = gr.Dropdown(["GPT", "Claude", "Gemini", "CodeQwen"],
                                label="Select Model", value="GPT", elem_classes=["model"])

        python_script.change(
            fn=lambda script: PYTHON_SCRIPTS[script],
            inputs=[python_script],
            outputs=[python]
        )

        comments_btn.click(
            fn=lambda: "",
            inputs=None,
            outputs=[python_with_comments]
        ).then(
            fn=generate_comments,
            inputs=[python, model],
            outputs=[python_with_comments]
        )

        return python_with_comments


# Tab to Generate Comprehensive Unit Tests
def unit_tests_ui():
    with gr.Tab("Unit Tests"):
        gr.Markdown("""
        ## Generate Comprehensive Unit Tests
        This tab helps you create unit tests for your Python code automatically.
        - Paste your Python code into the **`Python Code`** textbox.
        - Choose a model (GPT, Claude, Gemini, or CodeQwen) to generate the unit tests.
        - Click the **`Generate Unit Tests`** button, and the generated unit tests will appear in the **`Python Code with Unit Tests`** textarea.
        Use these unit tests to ensure your code behaves as expected.
        """)
        with gr.Row():
            python = gr.Textbox(label="Python Code:", lines=20,
                                value=PYTHON_SCRIPTS["custom"], elem_classes=["python"])
            python_unit_tests = gr.TextArea(
                label="Python Code with Unit Tests:", interactive=True, lines=20, elem_classes=["python"])
        with gr.Row():
            python_script = gr.Dropdown(choices=list(PYTHON_SCRIPTS.keys(
            )), label="Select a Python script", value="custom", elem_classes=["model"])
            unit_tests_btn = gr.Button(
                "Generate Unit Tests", elem_classes=["button"])
            model = gr.Dropdown(["GPT", "Claude", "Gemini", "CodeQwen"],
                                label="Select Model", value="GPT", elem_classes=["model"])

        python_script.change(
            fn=lambda script: PYTHON_SCRIPTS[script],
            inputs=[python_script],
            outputs=[python]
        )

        unit_tests_btn.click(
            fn=lambda: "",
            inputs=None,
            outputs=[python_unit_tests]
        ).then(
            fn=generate_tests,
            inputs=[python, model],
            outputs=[python_unit_tests]
        )

        return python_unit_tests


# Tab to Convert Python Code to C++
def python_to_cpp_ui():
    with gr.Tab("Python to C++"):
        gr.Markdown("""
        ## Convert Python Code to C++
        This tab facilitates the conversion of Python code into C++.
        - Paste your Python code into the **`Python Code`** textbox.
        - Select your preferred model (GPT, Claude, Gemini, or CodeQwen) to perform the conversion.
        - Click **`Convert to C++`** to see the equivalent C++ code in the **`C++ Code`** textbox.
        Additional Features:
        - You can execute the Python or C++ code directly using the respective **`Run Python`** or **`Run C++`** buttons.
        - The output will appear in the respective result text areas below.
        """)
        with gr.Row():
            python = gr.Textbox(label="Python Code:", lines=20,
                                value=PYTHON_SCRIPTS["custom"], elem_classes=["python"])
            cpp = gr.Textbox(label="C++ Code:", interactive=True,
                             lines=20, elem_classes=["cpp"])
        with gr.Row():
            python_script = gr.Dropdown(choices=list(PYTHON_SCRIPTS.keys(
            )), label="Select a Python script", value="custom", elem_classes=["model"])
            convert_btn = gr.Button("Convert to C++", elem_classes=["button"])
            model = gr.Dropdown(["GPT", "Claude", "Gemini", "CodeQwen"],
                                label="Select Model", value="GPT", elem_classes=["model"])
        with gr.Row():
            run_python_btn = gr.Button(
                "Run Python", elem_classes=["run-button"])
            run_cpp_btn = gr.Button("Run C++", elem_classes=["run-button"])
        with gr.Row():
            python_out = gr.TextArea(
                label="Python Result:", lines=10, elem_classes=["python"])
            cpp_out = gr.TextArea(label="C++ Result:",
                                  lines=10, elem_classes=["cpp"])

        python_script.change(
            fn=lambda script: PYTHON_SCRIPTS[script],
            inputs=[python_script],
            outputs=[python]
        )

        convert_btn.click(
            fn=lambda: "",
            inputs=None,
            outputs=[cpp]
        ).then(
            fn=convert_code,
            inputs=[python, model],
            outputs=[cpp]
        )
        run_python_btn.click(run_python, inputs=[python], outputs=[python_out])
        run_cpp_btn.click(run_cpp, inputs=[cpp], outputs=[cpp_out])

        return cpp, python_out, cpp_out
