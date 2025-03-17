import { setupSidebar } from './modules/sidebar.js';
import { setupDropdown } from './modules/dropdown.js';
import { setupMiniMenu } from './modules/miniMenu.js';
import { displayFlashMessages } from './modules/flashMessages.js';
import { addRow } from './modules/exerciseTable.js';
import { validatePasswords } from './modules/utils.js';

document.addEventListener('DOMContentLoaded', () => {
    const elements = {
        themeToggle: document.querySelectorAll('#theme-toggle-1, #theme-toggle-2'),
        sidebarCheckbox: document.getElementById('sidebar-checkbox'),
        sidebar: document.getElementById('sidebar'),
        dropdownButton: document.getElementById('dropdownButton'),
        dropdownList: document.getElementById('dropdownList'),
        configButton: document.getElementById('config'),
        miniMenu: document.getElementById('mini-menu'),
        configIcon: document.getElementById('config__icon'),
        flashMessages: 'flash-messages',
        exercisesData: 'exercises-data',
    };

    elements.themeToggle.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const checked = toggle.checked;
            elements.themeToggle.forEach(otherToggle => (otherToggle.checked = checked));
        });
    });

    setupSidebar(elements.sidebarCheckbox, elements.sidebar);
    setupDropdown(elements.dropdownButton, elements.dropdownList);
    setupMiniMenu(elements.miniMenu, elements.configButton, elements.configIcon);
    displayFlashMessages(elements.flashMessages);

    window.addRow = (day) => addRow(day, elements.exercisesData);

    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.onsubmit = validatePasswords;
    }
});