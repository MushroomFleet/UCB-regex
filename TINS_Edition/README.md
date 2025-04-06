# 🌈✨ Ultimate Care Bear (UCB) Text Transformer (Python Desktop App) ✨🌈

![app screenshot](https://github.com/fernicar/UCB_TINS_Edition/TINS_Edition/images/app_screenshot.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

> **Transform any text into the most positive, uplifting version possible using the power of AI!** This desktop application uses the Groq API to ensure your written communication radiates warmth, encouragement, and good energy.

**(Note: This is a Python/Tkinter implementation based on the concept described in the original UCB README.)**

<!-- Optional: Add a screenshot here later
![Screenshot of the UCB App](link_to_your_screenshot.png)
-->

## ✨ Features

-   **AI-Powered Transformation**: Leverages the Groq API (using models like Llama 3) to intelligently rewrite text with a positive focus.
-   **Desktop GUI**: Simple and intuitive graphical interface built with Tkinter.
-   **Command Line Interface**: Alternative CLI version for terminal users and automation.
-   **Multiple Input Options**: Paste text directly, upload text files (`.txt`), or use command line arguments.
-   **Timestamp Certification**: Each transformation automatically includes a timestamp.
-   **Copy Functionality**: Easily copy the transformed text to your clipboard.
-   **Clear Interface**: Buttons to quickly clear input and output fields.
-   **Real-time Status**: Provides feedback during the transformation process.

## 📋 Table of Contents

-   [Prerequisites](#-prerequisites)
-   [Installation](#-installation)
-   [Configuration (Important!)](#-configuration-important)
-   [Usage](#-usage)
-   [Command Line Usage](#-command-line-usage)
-   [How It Works](#-how-it-works)
-   [Contributing](#-contributing)
-   [License](#-license)

## 🔧 Prerequisites

-   **Python 3.x**: Download from [python.org](https://www.python.org/)
-   **pip**: Usually included with Python. Used to install packages.
-   **Groq API Key**: You **must** have an API key from [Groq](https://console.groq.com/keys).

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url> # Replace with your repo URL
    cd <your-repository-directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Groq API Key (Crucial Step):**
    You need to set your Groq API key as an environment variable. **Do not hardcode it in the script.**

    *   **Linux/macOS:**
        ```bash
        export GROQ_API_KEY='your_api_key_here'
        ```
    *   **Windows (Command Prompt):**
        ```bash
        set GROQ_API_KEY=your_api_key_here
        ```
    *   **Windows (PowerShell):**
        ```powershell
        $env:GROQ_API_KEY = 'your_api_key_here'
        ```
    *(You need to do this in the terminal session where you run the script, or configure it system-wide.)*

## ⚙️ Configuration (Important!)

The application relies entirely on the `GROQ_API_KEY` environment variable to authenticate with the Groq API. If this variable is not set correctly, the application will show an error message on startup and transformations will fail.

## 💡 Usage (GUI Version)

1.  **Ensure the `GROQ_API_KEY` environment variable is set.**
2.  **Run the application from your terminal:**
    ```bash
    python positive_text_transformer_tkinter.py
    ```
3.  **Enter Text**: Type or paste your text into the top input area.
4.  **(Optional) Upload a File**: Click "Choose File (.txt)" to load text from a file.
5.  **Transform**: Click the "Transform! 🌈" button. Wait for the AI to process the text (you'll see a status update).
6.  **View Results**: The positively transformed text appears in the bottom area, complete with a timestamp.
7.  **Copy**: Click "Copy Text ✨" to copy the result to your clipboard.
8.  **Clear**: Use the "Clear All 🧹" button to reset the input and output fields.

## 💻 Command Line Usage

The application also provides a command-line interface for terminal users or automation purposes:

1.  **Ensure the `GROQ_API_KEY` environment variable is set.**
2.  **Run the CLI version with direct text input:**
    ```bash
    python positive_text_transformer_cli.py --text "I'm having a really bad day. Everything is going wrong and I feel terrible."
    ```
    **Example output:**
    ```
    Transforming... Please wait...

    --- Transformed Text ---

    I'm embracing a challenging day as a chance to practice resilience and patience. Every obstacle is an opportunity to develop my problem-solving skills and grow as a person ✨.

    [Positively transformed on 2025-04-06 18:27:52] 🌈✨💖
    ```

3.  **Run the CLI version with a text file:**
    ```bash
    python positive_text_transformer_cli.py --file sample_text.txt
    ```
    **Example output:**
    ```
    Loaded text from sample_text.txt
    Transforming... Please wait...

    --- Transformed Text ---

    I'm excited about this project's growth potential! Despite the challenges, I'm proud of the time and effort I've invested so far. I'll take a short break to recharge and come back to it with renewed energy and a fresh perspective ✨.

    [Positively transformed on 2025-04-06 18:28:13] 🌈✨💖
    ```

## 🔄 How It Works

**GUI Version:**
1.  The **Tkinter GUI** provides the user interface elements (text boxes, buttons).
2.  User input (typed text or loaded file content) is captured.
3.  When "Transform!" is clicked, the input text is sent to the **Groq API** via the `groq` Python library.
4.  A specific **system prompt** instructs the Groq AI model (e.g., Llama 3) to rewrite the text in an overwhelmingly positive and encouraging "Care Bear" style.
5.  The AI generates the transformed text.
6.  The application receives the response, appends a **timestamp**, and displays it in the output area.

**CLI Version:**
1.  Command-line arguments (`--text` or `--file`) are parsed to get the input text.
2.  The input text is sent to the **Groq API** using the same underlying transformation logic.
3.  The transformed text is displayed in the terminal with the same timestamp and formatting.

## 👥 Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

Please ensure your code follows basic Python best practices.

## TINS Prompt used to gernerate the app from the original UCB's README.md
Read more at TINS repository (ThereIsNoSource.com)

![app screenshot](https://github.com/fernicar/UCB_TINS_Edition/TINS_Edition/images/TINS_prompt.png)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Spread positivity, one transformation at a time!*