import { toggleClass } from './utils.js';

export const setupMiniMenu = (menu, button, icon) => {
    if (button && menu && icon) {
        button.addEventListener('click', () => {
            toggleClass(menu, 'active');
            toggleClass(icon, 'rotate');
        });

        document.addEventListener('click', (e) => {
            if (menu && button && !menu.contains(e.target) && !button.contains(e.target)) {
                menu.classList.remove('active');
                icon.classList.remove('rotate');
            }
        });
    }
};