// Get HTML elements
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");

// Listen for button clicks
sendButton.addEventListener("click", handleSend);

// Show the user's message
function addMessage(sender, text, className) {
    chatMessages.innerHTML += `
        <div class="message ${className}">
            <strong>${sender}:</strong> ${text}
        </div>
    `;

    scrollToBottom();
}

// Scroll to the latest message
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Send request to FastAPI
async function sendToAPI(message) {

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    return await response.json();
}

async function handleSend() {
    // Read user input
    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    // Clear the input immediately
    messageInput.value = "";

    // Return focus to the input
    messageInput.focus();

    // Show the user's message
    addMessage("You", message, "user-message");

    // Send request to the API and get the response
    const response = await sendToAPI(message);

    // Show the AI reply
    addMessage("AI", response.reply, "ai-message");

};