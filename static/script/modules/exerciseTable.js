export const addRow = (day, dataElementId) => {
    const tableBody = document.getElementById(`${day}TableBody`);
    const row = document.createElement('tr');

    const createCell = (name, type) => {
        const cell = document.createElement('td');
        const input = document.createElement(type === 'select' ? 'select' : 'input');
        input.name = `${day}${name.charAt(0).toUpperCase() + name.slice(1)}`;

        if (type === 'select') {
            const dataElement = document.getElementById(dataElementId);
            JSON.parse(dataElement?.textContent || '[]').forEach(exercise => {
                const option = document.createElement('option');
                option.value = exercise.id;
                option.textContent = exercise.name;
                input.appendChild(option);
            });
        } else {
            input.type = type;
        }

        cell.appendChild(input);
        return cell;
    };

    row.appendChild(createCell('exercise', 'select'));
    row.appendChild(createCell('repetitions', 'number'));
    row.appendChild(createCell('sets', 'number'));
    tableBody?.appendChild(row);
};