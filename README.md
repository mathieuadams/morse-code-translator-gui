# morse-code-translator-gui
A simple Morse Code Translator with a graphical user interface built using Python and Tkinter. Easily convert between English text and Morse code in both directions. Great for educational purposes or beginner-level GUI projects.

🔤 Morse Code Translator with GUI 
This project is a Python program that allows users to translate English text into Morse code, and vice versa. It uses two main components:

A Morse_code class that handles the translation logic.

A MorseCodeUi class that creates a simple graphical user interface (GUI) using tkinter.

📘 Part 1: The Morse_code Class
This class stores a dictionary for translating between characters and Morse code, and it has two methods to perform the translations.

__init__(self)
Initializes a dictionary (conversion_table) that maps letters, digits, and punctuation to their corresponding Morse code.

For example, "a": ".-", "b": "-...", " " (space) becomes "/" in Morse.

text_to_Morse(self, s)
Converts text (e.g., "hello") into Morse code.

Steps:

Converts the input string to lowercase so that it matches the keys in the dictionary.

Loops through each character:

If the character exists in the dictionary, its Morse equivalent is added to a list, with a space after each Morse symbol.

Returns the joined Morse code string.

Morse_to_text(self, s)
Converts Morse code back into text.

Steps:

Adds an extra space at the end of the input to make sure the last Morse letter is processed.

Initializes two strings:

decipher: final translated message.

citext: temporary storage for a single Morse character.

Loops through each symbol:

If it's /, it adds a space (indicating a new word).

If it's not a space, it keeps building the current Morse letter.

When a space is encountered (end of a Morse letter), it:

Looks up the citext value in the dictionary (reverse lookup).

Appends the corresponding English character to decipher.

Clears citext for the next letter.

💻 Part 2: The MorseCodeUi Class (tkinter GUI)
This class creates a simple user interface for converting text <--> Morse code.

__init__(self)
Creates a tkinter window with a title and background color.

Sets up a Canvas to display the translated text.

Adds:

A label and entry box to convert English text to Morse.

A label and entry box to convert Morse to English.

Two buttons:

"Get Morse" to translate English into Morse.

"Get English" to translate Morse into English.

Starts the GUI with self.window.mainloop().

find_morse(self)
Triggered when the "Get Morse" button is clicked.

Gets the text from the entry field.

Uses the Morse_code class to convert it to Morse.

Displays the result on the canvas.

decode_morse(self)
Triggered when the "Get English" button is clicked.

Gets the Morse code from the entry field.

Uses the Morse_code class to convert it back to English.

Displays the result on the canvas.

✅ Summary
The app translates between English and Morse code.

The logic is handled in a class with a dictionary and two conversion methods.

The UI is built with tkinter, allowing easy interaction for users.