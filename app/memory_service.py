"""
Memory Service

Manages conversation history for each user session.
"""
MAX_MESSAGES = 20  # Maximum messages stored per conversation
conversations = {}


def add_message(session_id: str, role: str, content: str) -> None:
    """
    Add a message to a conversation.
    """

    if session_id not in conversations:
        conversations[session_id] = []

    conversations[session_id].append(
        {
            "role": role,
            "content": content,
        }
    )

    # Keep only the most recent messages
    if len(conversations[session_id]) > MAX_MESSAGES:
        conversations[session_id].pop(0)

def get_conversation(session_id: str):
    """
    Return the conversation history for a session.
    """

    return conversations.get(session_id, [])


def clear_conversation(session_id: str) -> None:
    """
    Clear a conversation.
    """

    conversations.pop(session_id, None)