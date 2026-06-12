import random
from datetime import datetime


def play_word_game():
    """Run a tiny word guessing game."""
    words = [
        ("python", "A popular programming language"),
        ("chat", "What a chatbot does"),
        ("code", "What programmers write"),
        ("data", "Information"),
    ]

    word, hint = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))

    while scrambled == word:
        scrambled = "".join(random.sample(word, len(word)))

    print("Novapy: Let's play a word game!")
    print(f"Novapy: Unscramble this word: {scrambled}")
    print(f"Novapy: Hint: {hint}")
    guess = input("You: ").strip().lower()

    if guess in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a wonderful day! 👋"

    if guess == word:
        return "Correct! Nice work. 🎉"

    return f"Not quite. The correct word was '{word}'."


def get_response(user_input):
    """Return a predefined reply based on the user's input."""
    text = user_input.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "howdy"]):
        return "Hi there! 👋 How can I help you today?"

    elif any(word in text for word in ["how are you", "how r you", "how do you do"]):
        return "I'm doing great, thanks for asking! 😊 How about you?"

    elif any(word in text for word in ["what is your name", "who are you", "your name"]):
        return "I'm Novapy a python chatbot! 🤖"

    elif any(word in text for word in ["time", "what time"]):
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}. ⏰"

    elif any(word in text for word in ["date", "today", "what day"]):
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}. 📅"

    elif any(word in text for word in ["help", "what can you do", "commands"]):
        return (
            "I can respond to:\n"
            "  • Greetings  (hello, hi, hey)\n"
            "  • How are you\n"
            "  • What is your name\n"
            "  • Time / Date\n"
            "  • Word game\n"
            "  • Jokes\n"
            "  • bye / exit  (to quit)"
        )

    elif any(word in text for word in ["word game", "play game", "game", "scramble"]):
        return play_word_game()

    elif any(word in text for word in ["joke", "tell me a joke", "funny"]):
        return "Why do programmers prefer dark mode? \n Because light attracts bugs! 🐛😄"

    elif any(word in text for word in ["bye", "goodbye", "exit", "quit", "see you"]):
        return "Goodbye! Have a wonderful day! 👋"

    else:
        return "Hmm, I didn't quite catch that. Type 'help' to see what I can do! 🤔"


def is_exit_command(user_input):
    """Return True if the user wants to quit."""
    return any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"])


def main():
    """Main loop: greet the user, listen for input, respond, repeat."""
    print("=" * 40)
    print("       Welcome to Novapy! 🤖")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 40)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Novapy: {response}\n")

        if is_exit_command(user_input):
            break


if __name__ == "__main__":
    main()
