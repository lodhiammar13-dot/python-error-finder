import streamlit as st

def explain_error_message(error_message):

    explanations = {
        "SyntaxError": (
            "Oops! Python got confused trying to read your code. Something about the structure isn’t quite right — "
            "this often happens when a colon, bracket, or parenthesis is missing, or when indentation is off. "
            "Take a close look at the line mentioned in the error."
        ),
        "TypeError": (
            "Ahh, this is a type mix-up. Python is trying to perform an operation, but the data types don’t match "
            "(for example, adding text to a number). Check what kind of values your variables hold."
        ),
        "NameError": (
            "Hmm, Python doesn’t recognize that name. It usually means the variable or function hasn’t been defined yet, "
            "or there’s a small spelling mistake somewhere."
        ),
        "IndexError": (
            "Looks like you tried to access a position in a list that doesn’t exist. The index might be too large, "
            "or the list could be shorter than you expected."
        ),
        "KeyError": (
            "Python tried to find that key in the dictionary but couldn’t. Double-check the key’s spelling and make sure "
            "it was added to the dictionary before you used it."
        ),
        "IndentationError": (
            "Python is very picky about spacing, and something isn’t lined up correctly. "
            "You may have mixed tabs and spaces or forgotten to indent after a statement like `if`, `for`, or `def`."
        ),
        "ValueError": (
            "The data type is correct, but the value itself doesn’t make sense for this operation. "
            "For example, trying to turn the word 'hello' into a number."
        ),
        "AttributeError": (
            "You’re trying to use something that doesn’t belong to that object. "
            "This usually happens when calling a method or attribute that the variable’s type doesn’t have."
        ),
        "ImportError": (
            "Python tried to import something but couldn’t find it. The module might not be installed, "
            "or the name could be misspelled."
        ),
        "ModuleNotFoundError": (
            "Python can’t find the module you’re trying to import. It may not be installed yet. "
            "Try installing it using `pip install module_name`."
        ),
        "ZeroDivisionError": (
            "Math says no 😅 You tried dividing a number by zero, which isn’t allowed. "
            "Check the value of the denominator before dividing."
        ),
        "FileNotFoundError": (
            "Python looked for a file but couldn’t find it at the given path. "
            "Make sure the file exists and the path is spelled correctly."
        ),
        "PermissionError": (
            "Python found the file, but it doesn’t have permission to access it. "
            "You might need to close the file in another program or run your script with proper permissions."
        ),
        "UnboundLocalError": (
            "You’re trying to use a local variable before assigning a value to it. "
            "Make sure the variable is set before it’s used inside the function."
        ),
        "AssertionError": (
            "An `assert` statement failed, which means a condition you expected to be true wasn’t. "
            "Check the logic of the condition being tested."
        ),
        "StopIteration": (
            "An iterator has no more items to give. This usually appears when manually looping through "
            "an iterator and it reaches the end."
        ),
        "OverflowError": (
            "The number became too large for Python to handle in that operation. "
            "This can happen with extremely big calculations."
        ),
        "RecursionError": (
            "Your function called itself too many times and hit Python’s recursion limit. "
            "There might be a missing base case or the recursion isn’t stopping properly."
        )
    }

    for key in explanations:
        if key.lower() in error_message.lower():
            return explanations[key]

    return "Hmm… I don’t recognize this error yet. Try checking the full message or line number for more clues."

def main():
    
    st.set_page_config(
        page_title="Python Error Message Translator",
        page_icon="🐍",
        layout="centered",
        initial_sidebar_state="auto"
    )
    st.title("🐍 Python Error Message Translator")
    st.write("Paste a Python error message and I'll explain it in simple terms.")

    st.warning("**Note:** This tool is for educational purposes and may not cover all error messages. Always refer to official documentation for critical issues.")
    st.warning("**Disclaimer:** The explanations provided are simplified and may not capture all nuances of the error. Use this as a starting point for understanding.")
    st.caption("write down only the error message, without any code snippets or additional context. for example: TypeError, not 'TypeError: unsupported operand type(s) for +: 'int' and 'str''")
    error_message = st.text_area("Error Message", height=150)

    if st.button("Translate"):
        if error_message.strip() == "":
            st.warning("Please enter an error message to translate.")
        else:
            explanation = explain_error_message(error_message)
            st.success("Here’s what’s going on:")
            st.markdown(explanation)

# This line actually RUNS your app
if __name__ == "__main__":
    main()
