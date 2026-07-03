// Get HTML elements
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");

// Listen for button clicks
sendButton.addEventListener("click", async function () {

    // Read user input
    const message = messageInput.value;

    // Show the user's message
    chatMessages.innerHTML += `
        <div class="message user-message">
            <strong>You:</strong> ${message}
        </div>
    `;

    // Send request to FastAPI
    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    // Read the JSON response
    const data = await response.json();

    // Show the AI reply
    chatMessages.innerHTML += `
        <div class="message ai-message">
            <strong>AI:</strong> ${data.reply}
        </div>
    `;

    // Clear the input box
    messageInput.value = "";

    // Put the cursor back in the input
    messageInput.focus();

    // Scroll to the latest message
    chatMessages.scrollTop = chatMessages.scrollHeight;

});