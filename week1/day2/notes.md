# Day 2 Notes

## Overview
- This folder contains `sys_temp.py`.
- The script demonstrates a simple Groq Chat Completions request using a shared root `venv`.

## Key Concepts
- Loading environment variables with `python-dotenv`
- Initializing a Groq client with an API key
- Sending a chat completion request with a prompt
- Printing the model response

## Files
- `sys_temp.py`: requests a single chat completion and prints the result.

## Notes
- This folder relies on the repository root virtual environment and shared dependency configuration.
- Ensure `GROQ_API_KEY` is defined in the root `.env` file.

## Next Steps
1. Activate the root `venv` from the repository root.
2. Run `week1/day2/sys_temp.py`.
3. Verify the model response and update this note if needed.
