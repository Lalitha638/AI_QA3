import re

def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # Exit
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for using Library Chatbot. Goodbye!"

    # Greeting
    if re.search(r"\b(hi|hello|hey)\b", text):
        return "Hello! Welcome to the Library Assistant. How can I help you?"

    # Book search
    if re.search(r"\b(find book|search book|book availability|available books)\b", text):
        return "You can search books using the library catalog system."

    # Library timings
    if re.search(r"\b(timing|hours|open|close|library time)\b", text):
        return "Library is open from 9 AM to 6 PM Monday to Saturday."

    # Membership
    if re.search(r"\b(membership|join library|library card|register)\b", text):
        return "To get library membership, please fill the registration form and submit ID proof."

    # Fine info
    if re.search(r"\b(fine|late fee|penalty)\b", text):
        return "Late return fine is ₹5 per day per book."

    # Issue books
    if re.search(r"\b(issue book|borrow book|take book)\b", text):
        return "You can issue up to 3 books for 14 days."

    # Return books
    if re.search(r"\b(return book|submit book)\b", text):
        return "Return books at the issue counter before due date."

    return "Sorry, I didn't understand. Please ask about books, timings, membership, or fines."


def library_chatbot():
    print("LibraryBot: Welcome to Library Assistant")
    print("Type 'bye' to exit\n")

    while True:
        user = input("You: ")
        response = get_response(user)
        print("LibraryBot:", response)

        if user.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    library_chatbot()
