import openai


def chat_with_bot():
    openai.api_key = "Your open Ai api-key"

    print("You are chatting with Marv, a sarcastic chatbot. Type 'exit' to end the conversation.")

    user_input = input("You: ")
    messages = [
        {
            "role": "system",
            "content": "You are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    while user_input.lower() != "exit":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=256
        )

        bot_reply = response["choices"][0]["message"]["content"]
        print("Marv:", bot_reply)

        user_input = input("You: ")
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )


if __name__ == "__main__":
    chat_with_bot()
