import "./tree.css";
var jq = require('jquery')
require('jstree')

function render({ model, el }) {
	console.log('TDATA', model.get("data"))
	console.log('ELT', el)
	el.classList.add("awitree");
	jq(el).jstree({
		core: {
			check_callback: false,
			multiple: model.get("multiple"),
			animation: model.get("animation"),
			data: [model.get("data")]
		},
		search: {},
		plugins: ['wholerow', 'state', 'search']
	}).on('changed.jstree', (_e, data) => {
		var i, j, r = [];
		for (i = 0, j = data.selected.length; i < j; i++) {
			r.push(data.instance.get_node(data.selected[i]));
		}
		if (r.length > 0) {
			console.log('Selected Nodes : ', r)
			model.set("selected_nodes", r)
			model.save_changes();
		}
	});
}

export default { render };
