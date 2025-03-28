import marimo

__generated_with = "0.11.31"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import awitree as awit
    return awit, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Simple Interface to jstree with AnyWidget
        `awitree` provides a AnyWidget interface to `jsTree` a jquery plugin, that buids interactive trees in browser.

        To create a tree, we pass a python dictionary with the expected format specified for jstree given [here](https://www.jstree.com/docs/json/).
        ```python
        # Expected format of the node (there are no required fields)
        {
          id          : "string" # will be autogenerated if omitted
          text        : "string" # node text
          icon        : "string" # string for custom
          state       : {
            opened    : bool  # is the node open
            disabled  : bool  # is the node disabled
            selected  : bool  # is the node selected
          },
          children    : []  # array of strings or objects
          li_attr     : {}  # attributes for the generated LI node
          a_attr      : {}  # attributes for the generated A node
        }
        ```
        This python dictionary is passed to the javascript as a JSON object, which is rendered by jstree. When the next cell is run, it should render the tree as follows:
        ![](data:image/png;base64,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)
        """
    )
    return


@app.cell
def _(awit, mo):
    tree_data = {
        "id": "0",
        "text":"Main Root",
        "state": {"open" : True},
        "children" : [
            {"id": "1", "text" : "Sub Node 1", "children":[]},
            {"id": "2", "text" : "Sub Node 2", "children":[]},
            {"id": "3", "text" : "Sub Node 3", "children":[]},
        ]
    }
    #
    rtree = awit.Tree(data=tree_data)
    motree = mo.ui.anywidget(rtree)
    motree
    return motree, rtree, tree_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Explorer view with `selected_nodes` trait
         `awitree.Tree` has a `selected_nodes` trait which keeps track of the selected nodes via the `traitlets` library. Using a dictionary of panels, an explorer-like User Interface can be accomplished as shown in the next cell.

         When the next cell is run, it should render as shown below: 
         ![](data:image/png;base64,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)
        """
    )
    return


@app.cell
def _(awit, mo, tree_data):
    panel_map = {
      "0":  mo.vstack([mo.ui.text(label="A"), mo.ui.text_area(label="B")]),
      "1":  mo.vstack([mo.ui.text(label="C"), mo.ui.text_area(label="D")]),
      "2":  mo.vstack([mo.ui.text(label="E"), mo.ui.text_area(label="F")]),
      "3":  mo.vstack([mo.ui.text(label="G"), mo.ui.text_area(label="H")]),
    }
    exrtree = awit.Tree(data=tree_data)
    moextree = mo.ui.anywidget(exrtree)
    return exrtree, moextree, panel_map


@app.cell
def _(exrtree, mo, moextree, panel_map):
    rt_selected = (
        panel_map[exrtree.selected_nodes[0]["id"]]
        if (
            exrtree.selected_nodes and 
            len(exrtree.selected_nodes) > 0 and 
            (exrtree.selected_nodes[0]["id"] in panel_map)
        ) else None
    )

    vxst = mo.hstack(
        [
            moextree,
            rt_selected  if rt_selected else mo.vstack([])
        ]
    )
    vxst
    return rt_selected, vxst


if __name__ == "__main__":
    app.run()
