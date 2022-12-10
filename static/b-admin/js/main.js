document.addEventListener('DOMContentLoaded', () => {
    const choiceFields = document.getElementsByName('choice');

    const hideElement = (array) => {
        array.forEach(el => {
            el.style.display = 'None';
        })
    }

    const showElement = (el) => {
        el.style.display = 'block';
    }


    const linkRow = document.querySelector('.field-file_string');
    const fileRow = document.querySelector('.field-file');

    const fileField = document.querySelector('#id_file');
    const linkField = document.querySelector('#id_file_string');

    const clearElements = () => {
        hideElement([linkRow, fileRow]);
    }

    const setNameElement = (el) => {
        fileField.setAttribute('id', 'asd');
        fileField.setAttribute('name', 'asd');
        el.setAttribute('id', 'id_file');
        el.setAttribute('name', 'file');

    }

    clearElements();
    showElement(fileRow);
    choiceFields.forEach(field => {
        field.addEventListener('click', (e) => {
            if (e.target.value === 'Link') {
                clearElements();
                showElement(linkRow);
                setNameElement(linkField);
            }
            else {
                clearElements();
                showElement(fileRow);
                setNameElement(fileField);
            }

        });
    });
})

