import os
import datetime
import argparse
from groq import Groq, GroqError

def get_groq_client():
    """Initializes and returns the Groq client, checking for API key."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("API Key Error: GROQ_API_KEY environment variable not found.")
        print("Please set it before running the application.")
        return None
    return Groq(api_key=api_key)

def transform_text_with_groq(client, input_text):
    """Uses Groq API to transform text into a positive version."""
    if not client or not input_text:
        return ""

    system_prompt = (
        "You are the Ultimate Care Bear Text Transformer. Your sole purpose is to "
        "transform negative text into constructive, positive alternatives. "
        "Follow these specific guidelines:\n"
        "1. Identify negative words, phrases, and sentence structures.\n"
        "2. Replace them with constructive, positive alternatives that maintain the original meaning.\n"
        "3. Focus on turning problems into opportunities and complaints into suggestions.\n"
        "4. Add occasional positive emojis (like 💖, ✨, 🌈) but use them sparingly.\n"
        "5. Keep the same topic and intent, just phrase it constructively.\n"
        "6. Do NOT create a conversation or respond as if talking to the user.\n"
        "7. Simply output the transformed version of the input text.\n\n"
        "Examples:\n"
        "- 'I'm angry about this problem' → 'I'm passionate about solving this opportunity 💖'\n"
        "- 'This is a difficult challenge that seems impossible' → 'This is a growth-oriented opportunity that seems not yet possible ✨'\n"
        "- 'The project failed because of too many mistakes' → 'The project was a learning experience because of growth opportunities 🌈'\n\n"
        "Directly output ONLY the transformed text, without any explanation, preamble, or sign-off."
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": input_text,
                }
            ],
            # Choose a model - llama3-8b is often good for creative tasks
            model="llama3-8b-8192",
            temperature=0.7, # Allow some creativity
            max_tokens=1024,
            top_p=1,
            stop=None,
        )
        return chat_completion.choices[0].message.content

    except GroqError as e:
        print(f"Groq API Error: Failed to transform text: {e}")
        return f"[Error transforming text: {e}]"
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return "[Unexpected error during transformation]"

def main():
    parser = argparse.ArgumentParser(description="Ultimate Care Bear Text Transformer CLI")
    parser.add_argument("--text", help="Text to transform")
    parser.add_argument("--file", help="Path to a text file to transform")
    parser.add_argument("--output", help="Path to save the transformed text")
    args = parser.parse_args()

    # Get the Groq client
    groq_client = get_groq_client()
    if not groq_client:
        return

    # Get the input text
    input_text = ""
    if args.text:
        input_text = args.text
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                input_text = f.read()
            print(f"Loaded text from {args.file}")
        except Exception as e:
            print(f"Error loading file: {e}")
            return
    else:
        print("Please provide text to transform using --text or --file")
        return

    if not input_text.strip():
        print("No text to transform")
        return

    # Transform the text
    print("Transforming... Please wait...")
    transformed = transform_text_with_groq(groq_client, input_text)

    # Append timestamp
    if transformed and not transformed.startswith("[Error"):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        final_text = f"{transformed}\n\n[Positively transformed on {timestamp}] 🌈✨💖"
    else:
        final_text = transformed  # Show error message if transformation failed

    # Output the transformed text
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(final_text)
            print(f"Transformed text saved to {args.output}")
        except Exception as e:
            print(f"Error saving to file: {e}")
    else:
        print("\n--- Transformed Text ---\n")
        print(final_text)
        print("\n-----------------------\n")

if __name__ == "__main__":
    main()
