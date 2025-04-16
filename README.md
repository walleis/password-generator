# Password Generator

## Description

This Python script generates a random password based on user-specified criteria. It prompts the user to define the desired number of letters, symbols, and numbers to include in the password. The script then randomly selects characters from predefined lists and shuffles them to create a strong, unpredictable password.

## How to Use

1.  **Run the script:** Execute the Python script in your terminal or Python environment.
2.  **Enter password criteria:** The program will ask you three questions:
    * "How many letters would you like in your password?" - Enter the desired number of letters and press Enter.
    * "How many symbols would you like?" - Enter the desired number of symbols and press Enter.
    * "How many numbers would you like?" - Enter the desired number of numbers and press Enter.
3.  **View the generated password:** After you provide the input, the program will generate a random password based on your specifications and print it to the console.

## Functionality

* **Character Sets:** Utilizes three lists: `letters` (containing both lowercase and uppercase English alphabets), `numbers` (containing digits 0-9), and `symbols` (containing common special characters).
* **User Input:** Prompts the user for the desired count of letters, symbols, and numbers in the password.
* **Random Selection:** Uses the `random.choice()` function to randomly pick characters from each of the defined lists based on the user's input.
* **Password List Creation:** Appends the randomly selected letters, symbols, and numbers to a list called `passwordlist`.
* **Shuffling:** Employs the `random.shuffle()` function to randomize the order of the characters within the `passwordlist`. This ensures that the generated password is not predictable based on the order of character types added.
* **String Conversion:** Iterates through the shuffled `passwordlist` and concatenates each character to form a single string, which represents the final generated password.
* **Output:** Prints the randomly generated password to the console.

## Requirements

* Python 3.x (The `random` module is a built-in Python library, so no additional installation is required.)

## Installation

No specific installation is needed. Save the provided code as a `.py` file (e.g., `password_generator.py`) and run it using a Python interpreter.

## Code Explanation

* **`letters`:** A list containing all lowercase and uppercase English alphabet letters.
* **`numbers`:** A list containing the digits 0 through 9.
* **`symbols`:** A list containing common special characters.
* **`passwordlist`:** An empty list initialized to store the randomly selected characters before shuffling.
* **Welcome Message:** Prints a welcome message to the user.
* **User Input Prompts:** Prompts the user to enter the desired number of letters (`nr_letters`), symbols (`nr_symbols`), and numbers (`nr_numbers`). The input is converted to integers using `int()`.
* **Character Selection Loops:**
    * The first `for` loop iterates `nr_letters + 1` times (note: the loop should ideally run `nr_letters` times). In each iteration, a random letter is chosen from the `letters` list using `random.choice(letters)` and appended to the `passwordlist`.
    * The second `for` loop iterates `nr_symbols + 1` times (again, ideally `nr_symbols` times), randomly choosing and appending symbols from the `symbols` list.
    * The third `for` loop iterates `nr_numbers + 1` times (ideally `nr_numbers` times), randomly choosing and appending numbers from the `numbers` list.
* **Shuffling:** `random.shuffle(passwordlist)` shuffles the elements (characters) within the `passwordlist` in place, making the order random.
* **String Conversion:**
    * `passwordstring = ""` initializes an empty string variable.
    * The `for` loop iterates through each `char` in the `passwordlist`.
    * `passwordstring += char` appends the current character to the `passwordstring`.
* **Output:** `print(passwordstring)` displays the final randomly generated password as a string.
