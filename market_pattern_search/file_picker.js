function render({model, el}) {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.zip, .csv';

    const paragraph = document.createElement('p');
    paragraph.style.display = 'none';

    const submit = document.createElement('button');

    el.appendChild(input);
    el.appendChild(paragraph);
    el.appendChild(submit);

    function updateText() {
        if (model.get('confirmed_filename')) {
            paragraph.textContent = `Uploaded file: ${model.get('confirmed_filename')}`;
            paragraph.style.display = 'block';
        } else if (model.get('pending_filename')) {
            paragraph.textContent = `Selected file: ${model.get('pending_filename')}`;
            paragraph.style.display = 'block';
        } else {
           paragraph.style.display = 'none';
        }
    }

    input.addEventListener('change', (event) => {
        if (!event.target.files.length) {
            return;
        }
        const file = event.target.files[0];
        if (file) {
            model.set("pending_filename", file.name)
            model.save_changes()
        }
        updateText()
    });

    submit.addEventListener('click', () => {
        if (model.get('pending_filename')) {
            model.set("confirmed_filename", model.get('pending_filename'))
            model.save_changes()
        }
        updateText()
    });

    // Initial render
    updateText()
}

export default {
    render
};