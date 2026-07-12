# Day 3 Notes

## Overview
- This folder contains `tokens.py`.
- The script shows how to send multiple prompts to the Groq Chat Completions API and inspect token usage.

## Key Concepts
- Looping through multiple prompts
- Sending each prompt as a separate chat completion request
- Reading token usage from the API response
- Using a shared root `venv` for the full repository

## Files
- `tokens.py`: sends 3 prompts to the model and prints token usage details.

## Notes
- This folder uses the repository root virtual environment and shared dependency configuration.
- Ensure `GROQ_API_KEY` is defined in the root `.env` file.

## Next Steps
1. Activate the root `venv` from the repository root.
2. Run `week1/day3/tokens.py`.
3. Observe token usage output and update this note if needed.
