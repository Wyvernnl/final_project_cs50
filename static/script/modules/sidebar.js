export const setupSidebar = (checkbox, sidebar) => {
    checkbox?.addEventListener('change', () => {
        sidebar.style.left = checkbox.checked ? '0px' : '-250px';
    });
};
