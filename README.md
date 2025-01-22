
# DocuPy

## Overview

**DocuPy** is an all-in-one tool designed to enhance productivity and streamline Python code workflows. With a user-friendly interface built using Gradio, DocuPy provides powerful utilities for documenting, testing, and converting Python code into C++. By leveraging state-of-the-art AI models like GPT, Claude, Gemini, and CodeQwen, this application offers developers advanced capabilities to:

1. **Generate Docstrings and Comments**: Automatically add clear, concise, and meaningful documentation and inline comments to your Python code.
2. **Create Comprehensive Unit Tests**: Quickly generate robust unit tests to ensure your code behaves as expected, helping maintain quality and reliability.
3. **Convert Python Code to C++**: Seamlessly translate Python code into C++ while providing options to execute and review the outputs directly within the app.

DocuPy's intuitive tab-based design ensures that each feature is accessible and straightforward to use. Developers can focus on coding while the app takes care of essential but time-consuming tasks like documentation, testing, and code translation. Whether you’re a beginner or an experienced developer, DocuPy is tailored to make your coding experience efficient and enjoyable.

---

## Features

**1. Document Code with Docstrings and Comments**  
**2. Generate Comprehensive Unit Tests**  
**3. Convert Python Code to C++**  
**4. Running Code Functions**

### **⚠️ Important Warning**

The functions that dynamically execute Python or C++ code provided as input are **extremely powerful** but also **highly dangerous** if the input code is not trusted. 

#### Potential Risks:
- 🚫 **Deleting files or directories**: The code could remove important files or directories.
- 🕵️ **Stealing sensitive data**: Access to environment variables, credentials, or other private information.
- 💻 **Running arbitrary commands**: Malicious commands can be executed, compromising the system.

**Recommendation:**
Only use this functionality in controlled environments and with trusted input.

---

## Setup 

### Clone the Repository
```bash
git clone https://github.com/emads22/DocuPy.git
cd DocuPy
```

### Install Dependencies
If you’re running this project on **Google Colab**, ensure you install the required libraries by executing the following command:

```bash
!pip install -q openai anthropic python-dotenv gradio huggingface_hub transformers
```

For local installations, navigate to the project directory and activate the provided Conda environment to ensure all dependencies are installed:

```bash
conda env create -f .\docupy_env.yml
conda activate docupy
```

### Set Up API Keys
DocuPy uses various AI models that require API keys. Follow these steps to configure them:

- **Closed-Tier Models (GPT, Claude, Gemini):** Obtain API keys for each model from their respective providers and add them to a `.env` file in the project directory.
  
  Example `.env` structure:
  ```env
  OPENAI_API_KEY=your_openai_api_key
  ANTHROPIC_API_KEY=your_anthropic_api_key
  GOOGLE_API_KEY=your_google_api_key
  ```

- **CodeQwen (Open-Source):** Obtain a Hugging Face token by logging in to your Hugging Face account and generating an access token. Use this token to access a dedicated endpoint for the CodeQwen model.
  ```env
  HF_TOKEN=your_huggingface_token
  CODE_QWEN_URL=your_hugging_face_open_source_model_dedicated_endpoint
  ```

Make sure to include these values in your `.env` file to ensure the application can access the required APIs.

### Special Instructions for Colab Users
When running DocuPy on Colab, avoid storing API keys in a `.env` file. Instead, add them as Colab secrets for security.

Ensure all required environment variables are set before launching the app.

---

## Usage

### Running the App
1. Navigate to the project directory.
2. Start the application by running:
   ```bash
   python app.py
   ```
3. The app will launch in your default web browser. If it does not open automatically, follow the URL provided in the terminal.

### Using the Features

#### 1. Document Code with Docstrings and Comments
- Navigate to the "Docstrings & Comments" tab.
- Paste your Python code into the **`Python Code`** textbox.
- Select a model (e.g., GPT, Claude, Gemini, CodeQwen) to process the code.
- Click the **`Add Docstrings & Comments`** button to generate the documented code.
- Review and copy the enhanced code from the output textbox.

#### 2. Generate Comprehensive Unit Tests
- Open the "Unit Tests" tab.
- Paste your Python code into the **`Python Code`** textbox.
- Choose a model to generate the unit tests.
- Click the **`Generate Unit Tests`** button to view the generated test cases in the output textbox.

#### 3. Convert Python Code to C++
- Go to the "Python to C++" tab.
- Paste your Python code into the **`Python Code`** textbox.
- Select a model to perform the conversion.
- Click the **`Convert to C++`** button to generate the equivalent C++ code.
- Optionally, execute the generated Python or C++ code using the respective **`Run`** buttons and review the outputs in the result areas.

#### 4. Additional Notes
- Ensure your API keys are set up before using closed-tier models.
- For best performance, choose the model that aligns with your requirements.
- For security, avoid running untrusted code using the execution features.  

---

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues.
- Suggest new features or improvements.
- Submit pull requests with bug fixes or enhancements.

---

## Author
- **Emad**  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

---

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.



