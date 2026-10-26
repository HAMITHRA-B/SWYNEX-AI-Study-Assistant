# SWYNEX AI Study Assistant

A small Python + Streamlit prototype that integrates Google's Gemini API to generate student-friendly explanations for study questions.

## Features
- Ask questions in a simple web interface
- Choose Beginner, Intermediate, or Advanced explanations
- Choose short, step-by-step, bullet-point, or example-based answers
- Calls a pre-trained AI model through the Gemini API
- Keeps the API key outside the source code

## Tech stack
- Python
- Streamlit
- Google Gen AI Python SDK (`google-genai`)
- Gemini API

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository and open a terminal in the project folder.
3. Create and activate a virtual environment (recommended):

   **Windows PowerShell**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

5. Create a Gemini API key in Google AI Studio: https://aistudio.google.com/app/apikey

6. Create a local secrets file:
   - Make a copy of `.streamlit/secrets.toml.example`
   - Name the copy `secrets.toml` in the same `.streamlit` folder
   - Put your key between the quotation marks for `GEMINI_API_KEY`

   The real `secrets.toml` is ignored by Git and must not be uploaded.

7. Start the app:
   ```powershell
   streamlit run app.py
   ```

8. Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Example prompts
- Explain machine learning with an example.
- What is a Python list? Give a small code example.
- Explain photosynthesis step by step.

See [examples.md](examples.md) for more examples.

## How it works
1. The student enters a question and chooses an explanation style.
2. Streamlit validates that the question and API key are present.
3. The Google Gen AI SDK sends the prompt to the Gemini API.
4. The model-generated text is displayed in the app.

## Security
- Never commit API keys, `.env` files, or `.streamlit/secrets.toml`.
- If a key is accidentally published, revoke it and create a new one.
- API availability, quotas, model access, and charges depend on your Google AI Studio account and current API terms.

## Limitations
The model can generate incorrect or incomplete answers. Check important facts against textbooks or instructor-approved sources. This prototype does not store a student's question history in a database.

## Task
SWYNEX Internship — Task 2: Model or API Integration.
