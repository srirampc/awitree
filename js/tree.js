import "./tree.css";
var jq = require('jquery')
var jstree = require('jstree')

function render({ model, el }) {
	console.log(model.get("tdata"))
	console.log(el)
	el.classList.add("awitree");
	jq(el).jstree({
		core: {
			check_callback: true,
			multiple: false,
			animation: 0,
			data: [model.get("tdata")]
		},
		plugins: ['wholerow', 'state', 'search', 'contextmenu']
	}).on('changed.jstree', (e, data) => {
		var i, j, r = [];
		for (i = 0, j = data.selected.length; i < j; i++) {
			r.push(data.instance.get_node(data.selected[i]));
		}
		console.log('Selected : ', r)
	});
	console.log('RTV', jq(el).jstree(true))
}

export default { render };
