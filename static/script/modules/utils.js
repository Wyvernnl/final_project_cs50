export const toggleClass = (element, className) => {
    if (element) {
        element.classList.toggle(className);
    }
};

export const toggleDisplay = (element) => {
    if (element) {
        element.style.display = element.style.display === 'block' ? 'none' : 'block';
    }
};

export const setStyle = (element, styleProp, value) => {
    if (element) {
        element.style[styleProp] = value;
    }
};

export const validatePasswords = () => {
    const password = document.getElementById('password').value;
    const passwordRepeat = document.getElementById('password-repeat').value;

    if (password !== passwordRepeat) {
        alert('Passwords do not match. Please try again.');
        return false;
    }
    return true;
};