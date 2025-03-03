
import gradio as gr
from app_ui import docs_comments_ui, unit_tests_ui, python_to_cpp_ui
from app_config import UI_CSS

# Combine the tabs into the main UI and handle tab switching
with gr.Blocks(title="DocuPy", theme=gr.themes.Soft(), css=UI_CSS) as main_ui:
    gr.Markdown("""
    # DocuPy
    ### A Smart Documentation and Testing Assistant for Python Developers
    """)
    
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

if __name__ == "__main__":
    # Launch the app
    main_ui.launch(inbrowser=True)
