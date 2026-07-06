// Get HTML elements
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");

// Create a unique session ID for this browser tab
const sessionId = crypto.randomUUID();

// Listen for button clicks
sendButton.addEventListener("click", handleSend);

// Listen for Enter key presses
messageInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        handleSend();
    }
});

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

function setLoading(isLoading) {
    sendButton.disabled = isLoading;
    messageInput.disabled = isLoading;

    if (!isLoading) {
        messageInput.focus();
    }
}

function showLoadingIndicator() {

    const loadingMessage = document.createElement("div");

    loadingMessage.className = "message ai-message";
    loadingMessage.id = "loading-message";

    loadingMessage.innerHTML = `
        <strong>AI:</strong> Thinking...
    `;

    chatMessages.appendChild(loadingMessage);

    scrollToBottom();
}

function hideLoadingIndicator() {

    const loadingMessage = document.getElementById("loading-message");

    if (loadingMessage) {
        loadingMessage.remove();
    }

}

// Send request to FastAPI
async function sendToAPI(message) {

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            session_id: sessionId,
            message: message
        })
    });

    if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
    }

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

    // Show the user's message
    addMessage("You", message, "user-message");

    // Enter loading state
    setLoading(true);
    showLoadingIndicator();
    try {

        // Send request to the API
        const response = await sendToAPI(message);
        hideLoadingIndicator();
        // Show AI reply
        addMessage("AI", response.reply, "ai-message");

    } catch (error) {

        console.error(error);
        hideLoadingIndicator();
        addMessage(
            "AI",
            "Sorry, something went wrong. Please try again.",
            "ai-message"
        );

    } finally {

        // Always restore the UI
        setLoading(false);

    }
}