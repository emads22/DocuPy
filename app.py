
import gradio as gr
from app_ui import docs_comments_ui, unit_tests_ui, python_to_cpp_ui

# CSS styles for customizing the appearance of the Gradio UI elements.
css = """
.python { 
    background-color: #377ef0; 
    color: #ffffff; 
    padding: 0.5em; 
    border-radius: 5px; /* Slightly rounded corners */
}
.cpp { 
    background-color: #00549e; 
    color: #ffffff; 
    padding: 0.5em; 
    border-radius: 5px; 
}
.model { 
    background-color: #17a2b8; /* Vibrant cyan color */
    color: white; 
    font-size: 1.2em; 
    padding: 0.5em; 
    border: none; 
    border-radius: 5px; 
    cursor: pointer; 
}
.button { 
    height: 4em; 
    font-size: 1.5em; 
    padding: 0.5em 1em; 
    background-color: #e67e22; /* Vibrant orange */
    color: white; 
    border: none; 
    border-radius: 5px; 
    cursor: pointer; 
}
.run-button { 
    height: 3em; 
    font-size: 1.5em; 
    padding: 0.5em 1em; 
    background-color: #16a085; /* Rich teal color */
    color: white; 
    border: none; 
    border-radius: 5px; 
    cursor: pointer; 
}
.button:hover, .run-button:hover {
    background-color: #2c3e50; /* Dark navy for hover effect */
    color: #fff; 
}
"""

# Combine the tabs into the main UI and handle tab switching
with gr.Blocks(css=css) as main_ui:
    with gr.Tabs() as tabs:
        comments_output = docs_comments_ui()
        tests_output = unit_tests_ui()
        cpp_output, python_out, cpp_out = python_to_cpp_ui()

    # Reset outputs on tab switch
    tabs.select(
        fn=lambda: ["", "", "", "", ""],
        inputs=None,
        outputs=[comments_output,
                 tests_output,
                 cpp_output, python_out, cpp_out]
    )

# Launch the app
main_ui.launch(inbrowser=True)
