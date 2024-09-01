import anywidget
import traitlets
import ipywidgets as widgets
from pathlib import Path


class FilePickerWidget(anywidget.AnyWidget):
    _esm = Path(__file__).parent / "file_picker.js"
    value = traitlets.Unicode().tag(sync=True)

    # def __init__(self):
    #     super().__init__()
    #     self.out = widgets.Output()

    def get_selected_file(self):
        return self.value


# Usage
# file_picker = FilePickerWidget()
# display(file_picker)
# selected_file = file_picker.get_selected_file()
# print(f"Selected file: {selected_file}")
