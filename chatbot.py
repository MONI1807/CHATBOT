import ast
import operator
import random
from datetime import datetime


def _safe_calculate(expression):
    """Evaluate a basic math expression safely."""

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def _evaluate(node):
        if isinstance(node, ast.Expression):
            return _evaluate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
            return allowed_operators[type(node.op)](_evaluate(node.left), _evaluate(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed_operators:
            return allowed_operators[type(node.op)](_evaluate(node.operand))
        raise ValueError("Unsupported expression")

    tree = ast.parse(expression, mode="eval")
    return _evaluate(tree)


def run_calculator():
    """Run a small interactive calculator session."""
    print("\nNovapy: Calculator mode. Type a math expression like 2 + 3 * 4.")
    print("Novapy: Type 'back' to return to the chatbot or 'exit' to quit.")

    while True:
        expression = input("Calculator: ").strip()

        if not expression:
            continue

        lowered = expression.lower()
        if lowered in {"back", "menu"}:
            print("Novapy: Back to chat.\n")
            return False
        if lowered in {"bye", "goodbye", "exit", "quit"}:
            print("Novapy: Goodbye! Have a wonderful day! 👋")
            return True

        try:
            result = _safe_calculate(expression)
            print(f"Novapy: The result is {result}\n")
        except Exception:
            print("Novapy: I could not understand that expression. Try something like 12 / 3 + 4.\n")


def play_word_game():
    """Run a small word scrambling game."""
    words = [
        ("python", "A popular programming language"),
        ("chatbot", "What Novapy is"),
        ("keyboard", "You type on it"),
        ("memory", "It helps you remember"),
        ("binary", "A number system with two symbols"),
    ]
    word, hint = random.choice(words)
    scrambled = list(word)

    while True:
        random.shuffle(scrambled)
        scrambled_word = "".join(scrambled)
        if scrambled_word != word:
            break

    print("\nNovapy: Word Game time!")
    print(f"Novapy: Unscramble this word: {scrambled_word}")
    print(f"Novapy: Hint: {hint}")
    print("Novapy: Type 'exit' to stop playing.")

    attempts = 3
    while attempts > 0:
        guess = input("Word Game: ").strip().lower()

        if not guess:
            continue

        if guess in {"bye", "goodbye", "exit", "quit"}:
            print(f"Novapy: The word was '{word}'. See you next time!\n")
            return True

        if guess == word:
            print("Novapy: Correct! Nice work. 🎉\n")
            return False

        attempts -= 1
        if attempts > 0:
            print(f"Novapy: Not quite. Try again. Attempts left: {attempts}")
        else:
            print(f"Novapy: Out of attempts. The answer was '{word}'.\n")
            return False


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
            "  • Calculator\n"
            "  • Word game\n"
            "  • Jokes\n"
            "  • bye / exit  (to quit)"
        )

    elif any(word in text for word in ["joke", "tell me a joke", "funny"]):
        return "Why do programmers prefer dark mode? \n Because light attracts bugs! 🐛😄"

    elif any(word in text for word in ["bye", "goodbye", "exit", "quit", "see you"]):
        return "Goodbye! Have a wonderful day! 👋"

    else:
        return "Hmm, I didn't quite catch that. Type 'help' to see what I can do! 🤔"


def is_calculator_command(user_input):
    """Return True if the user wants to use the calculator."""
    text = user_input.lower()
    return any(word in text for word in ["calculator", "calc", "math mode"])


def is_word_game_command(user_input):
    """Return True if the user wants to play the word game."""
    text = user_input.lower()
    return any(word in text for word in ["word game", "game", "play game", "scramble"])


def is_exit_command(user_input):
    """Return True if the user wants to quit."""
    return any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"])


def main():
    """Main loop: greet the user, listen for input, respond, repeat."""
    print("=" * 80)
    print("       Welcome to Novapy! 🤖")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 80)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if is_calculator_command(user_input):
            should_exit = run_calculator()
            if should_exit:
                break
            continue

        if is_word_game_command(user_input):
            should_exit = play_word_game()
            if should_exit:
                break
            continue

        response = get_response(user_input)
        print(f"Novapy: {response}\n")

        if is_exit_command(user_input):
            break


if __name__ == "__main__":
    main()
