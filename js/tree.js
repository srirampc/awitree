import "./tree.css";
var jq = require('jquery')
require('jstree')

function render({ model, el }) {
	console.log('TDATA', model.get("tdata"))
	console.log('ELT', el)
	el.classList.add("awitree");
	jq(el).jstree({
		core: {
			check_callback: false,
			multiple: model.get("multiple"),
			animation: model.get("animation"),
			data: [model.get("tdata")]
		},
		search: {},
		plugins: ['wholerow', 'state', 'search']
	}).on('changed.jstree', (_e, data) => {
		var i, j, r = [];
		for (i = 0, j = data.selected.length; i < j; i++) {
			r.push(data.instance.get_node(data.selected[i]));
		}
		if (r.length > 0) {
			console.log('Selected R : ', r[0])
			model.set("selected", r[0])
			model.save_changes();
		}
	});
}

export default { render };
