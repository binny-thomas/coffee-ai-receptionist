def ask_ai(system_prompt: str, user_message: str) -> str:
    """
    Return a mock AI response.
    """

    message = user_message.lower().strip()

    if message == "hello":
        return "Hello! Welcome to Cafecap Coffee. How can I help you today?"

    if "coffee" in message:
        return (
            "We offer freshly roasted, 100% pure coffee powder "
            "with no chicory."
        )

    return (
        "Thank you for contacting Cafecap Coffee. "
        "Our AI Receptionist is ready to assist you."
    )