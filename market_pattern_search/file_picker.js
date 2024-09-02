// import { FileUploadView } from '@jupyter-widgets/controls';
const controlsVersion = window.JUPYTER_WIDGETS_CONTROLS_VERSION || '8.1.5';
const controls = await import(`https://esm.sh/@jupyter-widgets/controls@${controlsVersion}`);
//import FileUploadView from `https://esm.sh/@jupyter-widgets/controls@${controlsVersion}`


export class ExtendedFileUploadView extends controls.FileUploadView {
    render() {
        super.render()
        const fileInput = this.fileInput
        fileInput.addEventListener('change', event => {
            if (!fileInput.files || !fileInput.files.length) {
                return;
            }

            const file = fileInput.files[0];
            if (this.checkIfServerFile(file.name)) {
                console.log('Found server file {file.name}');
                event.stopImmediatePropagation();
            }
        }, useCapture=true);
    }

    checkIfServerFile(filename) {
        return true;
        // return new Promise((resolve) => {
        //     resolve(true);
        // });
        //     this.send({ event: 'check_server_file', filename }, this.callbacks());
        //     this.once('msg:custom', (msg) => {
        //         if (msg.event === 'server_file_result') {
        //             resolve(msg.is_server_file);
        //         }
        //     });
        // });
    }
}
