import "./tree.css";
var jq = require('jquery')
var jstree = require('jstree')

function render({ model, el }) {
	console.log(el)
	el.classList.add("awitree");
	jq(el).jstree({
		'core': {
			check_callback: true,
			multiple: false,
			animation: true,
			'data':
				[
					'Simple root node',
					{
						'text': 'Root node 2',
						'state': {
							'opened': true,
							'selected': true
						},
						'children': [
							{ 'text': 'Child 1' },
							'Child 2'
						]
					}
				]
		},
		'plugins': ['wholerow', 'checkbox']
	});
	console.log('RTV', jq(el).jstree(true))
	// let rdiv = document.createElement("div");
	// rdiv.innerHTML = `count is ${model.get("value")}`;
	// rdiv.addEventListener("click", () => {
	// 	model.set("value", model.get("value") + 1);
	// 	model.save_changes();
	// });
	// model.on("change:value", () => {
	// 	rdiv.innerHTML = `Count : ${model.get("value")}`;
	// });
	// el.classList.add("awitree");
	// el.appendChild(rdiv);
}

export default { render };
