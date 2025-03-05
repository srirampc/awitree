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
    multiple = traitlets.Bool(False).tag(sync=True)
    animation = traitlets.Int(0).tag(syn=True)
    selected = traitlets.Dict({}).tag(sync=True)
    tdata = traitlets.Dict({}).tag(sync=True)
