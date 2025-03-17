import { toggleDisplay } from './utils.js';

export const setupDropdown = (button, list) => {
    if (button && list) {
        button.addEventListener('click', () => toggleDisplay(list));
        document.addEventListener('click', (e) => {
            if (!list.contains(e.target) && !button.contains(e.target)) {
                list.style.display = 'none';
            }
        });
    }
};