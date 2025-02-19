// Get elements
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

// Basic bot responses
const botResponses = {
  "hi": "Greetings, user. Welcome to the system.",
  "how are you": "Processing... I'm fully operational.",
  "what is your name": "I am the Digital Guardian, at your service.",
  "default": "Error: Unknown query. Please try again."
};

// Function to send a message
function sendMessage(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message');
  if (sender === 'user') {
    messageDiv.classList.add('user-message');
    messageDiv.innerHTML = `<span class="glitchy">${message}</span>`;
  } else {
    messageDiv.classList.add('bot-message');
    messageDiv.innerHTML = `<span class="glitchy">${message}</span>`;
  }
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto scroll to latest message
}

// Handle user input
function handleUserInput() {
  const userText = userInput.value.trim().toLowerCase();
  if (userText !== "") {
    sendMessage(userText, 'user');
    const botReply = botResponses[userText] || botResponses["default"];
    setTimeout(() => sendMessage(botReply, 'bot'), 1000);
  }
  userInput.value = ""; // Clear input field
}

// Send button click event
sendButton.addEventListener('click', handleUserInput);

// Enter key press event
userInput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    handleUserInput();
  }
});
