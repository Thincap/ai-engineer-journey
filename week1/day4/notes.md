# Day 4 Notes

## What I learned
- How to build a simple Python script that uses Groq API.
- How to load environment variables using `python-dotenv`.
- How to send a prompt and read the model response.
- How to extract structured information from user text using an LLM.

## Key concepts
- `load_dotenv()` loads values from a `.env` file.
- `GROQ_API_KEY` must be set before running the script.
- The Groq client sends chat completions to the model.
- Prompt engineering helps guide the model to return useful output.

## Example workflow
1. Create a `.env` file with your API key.
2. Run the Python script.
3. Review the model output and adjust the prompt if needed.

## Notes
- Keep API keys private and do not commit them to Git.
- Use clear prompts for better results.
- Test the script with different example messages.
