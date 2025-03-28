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
        ```json
        // Expected format of the node (there are no required fields)
        {
          id          : "string" // will be autogenerated if omitted
          text        : "string" // node text
          icon        : "string" // string for custom
          state       : {
            opened    : boolean  // is the node open
            disabled  : boolean  // is the node disabled
            selected  : boolean  // is the node selected
          },
          children    : []  // array of strings or objects
          li_attr     : {}  // attributes for the generated LI node
          a_attr      : {}  // attributes for the generated A node
        }
        ```

        This python dictionary is passed to the javascript as a JSON object, which is rendered by jstree.
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

         `awitree.Tree` has a `selected_nodes` trait which keeps track of the selected nodes via the `traitlets` library. Using a dictionary of panels, an explorer-like User Interface can be accomplished as shown below.
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
