export const displayFlashMessages = (containerId) => {
    const flashMessagesElement = document.getElementById(containerId);
    if (flashMessagesElement) {
        const messages = JSON.parse(flashMessagesElement.textContent || '[]');
        messages.forEach(message => {
            const alertBox = document.createElement('div');
            alertBox.className = 'alert-box';
            alertBox.textContent = message;
            document.body.appendChild(alertBox);
            setTimeout(() => alertBox.remove(), 6000);
        });
    }
};
