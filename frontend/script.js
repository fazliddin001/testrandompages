function get_response(url) {
    return fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(resp => {
        if (!resp.ok) {
            throw new Error(`Bad Response ${resp.status}`);
        }
        return resp.json();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function change() {
    const url = "http://localhost:8000/";

    get_response(url).then(data => {
        if (Array.isArray(data)) {
            const body = document.getElementsByTagName("body")[0];
            body.innerHTML = '';

            for (let i = 0; i < data.length; i++) {
                const cart_data = data[i];
                if (cart_data.image_url && cart_data.caption) {
                    const cart = `\n
                        <div class="cart">
                            <div class="img">
                                <img src="${cart_data.image_url}" alt="image">
                            </div>
                            <div class="content">
                                <h1>${cart_data.caption}</h1>
                            </div>
                        </div>`;

                    body.innerHTML += cart

                } else {
                    console.warn('cart_data is missing required properties:', cart_data);
                }
            }
        } else {
            console.error('Expected an array of data but got:', data);
        }
    });
}

// change();
setInterval(change, 1000);
