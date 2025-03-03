import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("awitree")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class Tree(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "tree.js"
    _css = pathlib.Path(__file__).parent / "static" / "tree.css"
    name = traitlets.Unicode("Node").tag(sync=True)
    value = traitlets.Int(0).tag(sync=True)
