import marimo

__generated_with = "0.11.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import awitree as awi
    return awi, mo


@app.cell
def _(awi, mo):
    rtree = awi.Tree(data={
        "id": "0",
        "text":"Main Root",
        "state": {"open" : True},
        "children" : [
            {"id": "1", "text" : "Sub Node 1", "children":[]},
            {"id": "2", "text" : "Sub Node 2", "children":[]},
            {"id": "3", "text" : "Sub Node 3", "children":[]},
        ]
    })
    panel_map = {
      "0":  mo.vstack([mo.ui.text(label="A"), mo.ui.text_area(label="B")]),
      "1":  mo.vstack([mo.ui.text(label="C"), mo.ui.text_area(label="D")]),
      "2":  mo.vstack([mo.ui.text(label="E"), mo.ui.text_area(label="F")]),
      "3":  mo.vstack([mo.ui.text(label="G"), mo.ui.text_area(label="H")]),
    }
    motree = mo.ui.anywidget(rtree)
    motree
    return motree, panel_map, rtree


@app.cell
def _(mo, motree, panel_map, rtree):
    rt_selected = (
        panel_map[rtree.selected_nodes[0]["id"]]
        if (
            rtree.selected_nodes and 
            len(rtree.selected_nodes) > 0 and 
            (rtree.selected_nodes[0]["id"] in panel_map)
        ) else None
    )

    vxst = mo.hstack(
        [
            motree,
            rt_selected  if rt_selected else mo.vstack([])
        ]
    )
    vxst
    return rt_selected, vxst


@app.cell
def _(rtree):
    rtree
    return


if __name__ == "__main__":
    app.run()
