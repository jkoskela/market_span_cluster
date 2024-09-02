from typing import Callable

import anywidget
import pandas as pd
import traitlets
from pathlib import Path

from traitlets import observe

ParseFunction = Callable[[str], pd.DataFrame]


class FilePickerWidget(anywidget.AnyWidget):
    _esm = Path(__file__).parent / "file_picker.js"
    # Each instance of the class will have a different instance of these properties, which are synced
    # between the front-end js and back-end python.
    pending_filename = traitlets.Unicode().tag(sync=True)
    confirmed_filename = traitlets.Unicode().tag(sync=True)

    def __init__(self, parse: ParseFunction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse = parse
        self.parsed: pd.DataFrame = None

    def get_pending_filename(self):
        return self.pending_filename

    def get_confirmed_filename(self):
        return self.confirmed_filename

    def get_dataframe(self):
        return self.parsed

    @observe("confirmed_filename")
    def _on_confirmed_filename_changed(self, change):
        self.parsed = self.parse(self.confirmed_filename)
