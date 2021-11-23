async function postData(url, csrf, data) {
	let formData = new FormData();
	for (var k in data) {
		formData.append(k, data[k]);
	}

	const response = await fetch(url, {
		method: "POST",
		headers: {
			"X-CSRFToken": csrf,
			"X-Requested-With": "XMLHttpRequest"
		},
		body: formData
	});

	return response.json();
}
