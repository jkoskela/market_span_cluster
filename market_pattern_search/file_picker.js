import { createWidget } from 'https://esm.sh/@anywidget/react';
import { useState, useEffect } from 'https://esm.sh/react';

export default createWidget((props) => {
    const [selectedFile, setSelectedFile] = useState(null);

    useEffect(() => {
        if (selectedFile) {
            props.setValue(selectedFile.name);
        }
    }, [selectedFile]);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        setSelectedFile(file);
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            {selectedFile && (
                <p>Selected file: {selectedFile.name}</p>
            )}
        </div>
    );
});