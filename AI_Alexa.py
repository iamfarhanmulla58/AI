print("AI Interactive Media Assistant")
print("Type 'exit' to stop.")

while True:
    user = input("\nYou: ").lower()

    if user == "exit":
        print("AI: Goodbye!")
        break

    elif "news" in user:
        print("AI: Here are today's latest news topics.")

    elif "weather" in user:
        print("AI: Today's weather information is available.")

    elif "music" in user:
        print("AI: Playing your requested music.")

    elif "bbc" in user:
        print("AI: Opening BBC news and media.")

    elif "hello" in user or "hi" in user:
        print("AI: Hello! How can I help you?")

    else:
        print("AI: Sorry, I don't understand that request.")