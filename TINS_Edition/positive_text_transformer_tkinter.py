import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import os
import datetime
from groq import Groq, GroqError

# --- Configuration ---
APP_TITLE = "🌈✨ Ultimate Care Bear (UCB) Text Transformer ✨🌈"
WINDOW_GEOMETRY = "700x650"
INPUT_BG_COLOR = "#e0f7fa" # Light cyan
OUTPUT_BG_COLOR = "#fff9c4" # Light yellow
BUTTON_BG_COLOR = "#ffc1e3" # Pinkish
BUTTON_FG_COLOR = "#333333"
STATUS_FG_COLOR = "#00695c" # Teal

# --- Groq API Interaction ---
def get_groq_client():
    """Initializes and returns the Groq client, checking for API key."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        messagebox.showerror(
            "API Key Error",
            "GROQ_API_KEY environment variable not found.\n"
            "Please set it before running the application."
        )
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
        messagebox.showerror("Groq API Error", f"Failed to transform text: {e}")
        return f"[Error transforming text: {e}]"
    except Exception as e:
         messagebox.showerror("Error", f"An unexpected error occurred: {e}")
         return "[Unexpected error during transformation]"

# --- GUI Application Class ---
class UltimateCareBearApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.configure(bg='#f0f0f0') # Light grey background

        self.groq_client = get_groq_client()
        if not self.groq_client:
            self.root.quit() # Exit if API key is missing
            return

        # --- Widgets ---
        # Input Area
        tk.Label(root, text="Enter Text Here or Upload File:", font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(pady=(10, 2))
        self.input_text = scrolledtext.ScrolledText(root, height=10, width=80, wrap=tk.WORD, font=('Arial', 11), bg=INPUT_BG_COLOR)
        self.input_text.pack(pady=5, padx=10)

        # File Handling Frame
        file_frame = tk.Frame(root, bg='#f0f0f0')
        file_frame.pack(pady=5)
        self.choose_file_button = tk.Button(file_frame, text="Choose File (.txt)", command=self.load_file, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, font=('Arial', 10, 'bold'))
        self.choose_file_button.pack(side=tk.LEFT, padx=5)
        self.file_label = tk.Label(file_frame, text="No file selected", font=('Arial', 10), bg='#f0f0f0', fg='#555')
        self.file_label.pack(side=tk.LEFT)

        # Transform Button
        self.transform_button = tk.Button(root, text="Transform! 🌈", command=self.run_transformation, font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white', relief=tk.RAISED, borderwidth=3)
        self.transform_button.pack(pady=10)

        # Output Area
        tk.Label(root, text="Positively Transformed Text:", font=('Arial', 12, 'bold'), bg='#f0f0f0').pack(pady=(10, 2))
        self.output_text = scrolledtext.ScrolledText(root, height=10, width=80, wrap=tk.WORD, font=('Arial', 11), bg=OUTPUT_BG_COLOR, state=tk.DISABLED) # Start disabled
        self.output_text.pack(pady=5, padx=10)

        # Action Buttons Frame
        action_frame = tk.Frame(root, bg='#f0f0f0')
        action_frame.pack(pady=10)
        self.copy_button = tk.Button(action_frame, text="Copy Text ✨", command=self.copy_output, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, font=('Arial', 10, 'bold'))
        self.copy_button.pack(side=tk.LEFT, padx=10)
        self.clear_button = tk.Button(action_frame, text="Clear All 🧹", command=self.clear_all, bg='#ff9800', fg='white', font=('Arial', 10, 'bold')) # Orange clear button
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Status Label
        self.status_label = tk.Label(root, text="", font=('Arial', 10, 'italic'), bg='#f0f0f0', fg=STATUS_FG_COLOR)
        self.status_label.pack(pady=5)

    # --- Callback Methods ---
    def load_file(self):
        filepath = filedialog.askopenfilename(
            title="Select a Text File",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if not filepath:
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            self.input_text.delete('1.0', tk.END)
            self.input_text.insert('1.0', content)
            self.file_label.config(text=os.path.basename(filepath))
            self.status_label.config(text=f"Loaded file: {os.path.basename(filepath)}")
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to read file: {e}")
            self.status_label.config(text="Error loading file.")

    def run_transformation(self):
        original_text = self.input_text.get("1.0", tk.END).strip()
        if not original_text:
            messagebox.showwarning("Input Missing", "Please enter some text or load a file to transform.")
            return

        if not self.groq_client:
             messagebox.showerror("API Error", "Groq client not initialized. Check API Key.")
             return

        self.status_label.config(text="Transforming... Please wait... ⏳")
        self.root.update_idletasks() # Force UI update

        transformed = transform_text_with_groq(self.groq_client, original_text)

        # Append Timestamp
        if transformed and not transformed.startswith("[Error"):
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            final_text = f"{transformed}\n\n[Positively transformed on {timestamp}] 🌈✨💖"
        else:
             final_text = transformed # Show error message if transformation failed

        # Update Output Text
        self.output_text.config(state=tk.NORMAL) # Enable editing
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', final_text)
        self.output_text.config(state=tk.DISABLED) # Disable editing

        self.status_label.config(text="Transformation complete! 🎉")

    def copy_output(self):
        text_to_copy = self.output_text.get("1.0", tk.END).strip()
        if text_to_copy:
            self.root.clipboard_clear()
            self.root.clipboard_append(text_to_copy)
            self.status_label.config(text="Output copied to clipboard! 👍")
        else:
            self.status_label.config(text="Nothing to copy.")

    def clear_all(self):
        self.input_text.delete('1.0', tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.file_label.config(text="No file selected")
        self.status_label.config(text="Cleared.")

# --- Main Execution ---
if __name__ == "__main__":
    main_window = tk.Tk()
    app = UltimateCareBearApp(main_window)
    main_window.mainloop()