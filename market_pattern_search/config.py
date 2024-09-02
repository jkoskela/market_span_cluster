from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

import ipywidgets
from IPython.display import display, Javascript

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


def is_jupyter():
    try:
        from IPython import get_ipython
        if get_ipython() is None:
            return False
        if 'IPKernelApp' not in get_ipython().config:
            return False
        if 'jupyter' not in get_ipython().config['IPKernelApp']['connection_file']:
            return False
        return True
    except ImportError:
        return False


if is_jupyter():
    controls_version = ipywidgets.__version__

    display(Javascript(f"""
        window.JUPYTER_WIDGETS_CONTROLS_VERSION = '{controls_version}';
    """))

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
