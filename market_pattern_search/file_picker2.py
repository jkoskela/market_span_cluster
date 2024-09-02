from pathlib import Path

import ipywidgets as widgets
from ipywidgets import register
from traitlets import Unicode

from market_pattern_search.config import is_jupyter

if is_jupyter():
    from IPython.display import display, Javascript
    js = Path(__file__).parent / "file_picker.js"
    display(Javascript(js))

@register
class ExtendedFileUpload(widgets.FileUpload):
    _view_name = Unicode('ExtendedFileUploadView').tag(sync=True)
