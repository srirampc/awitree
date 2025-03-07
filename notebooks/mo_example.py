import marimo

__generated_with = "0.11.16"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import awitree as awi
    return awi, mo


@app.cell
def _(awi, mo):
    rtree = awi.Tree(tdata={
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
    vxst = mo.hstack(
        [
            motree,
            panel_map[rtree.selected["id"]]
            if rtree.selected and (rtree.selected["id"] in panel_map)
            else mo.vstack([])
        ]
    )
    vxst 
    return (vxst,)


@app.cell
def _(rtree):
    rtree
    return


if __name__ == "__main__":
    app.run()
