function generateImage() {
    const text = document.getElementById('text-input').value;
    if (!text) {
        alert("Please enter some text!");
        return;
    }

    document.getElementById('loader').style.display = 'block';
    document.getElementById('image-container').innerHTML = "";

    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loader').style.display = 'none';
        if (data.image_url) {
            document.getElementById('image-container').innerHTML = `
                <img src="${data.image_url}" class="img-fluid" style="max-width: 100%; border-radius: 10px;">
                <a href="${data.image_url}" download="generated_image.png" class="btn btn-success mt-3">Save Image</a>
            `;
        } else {
            alert("Error generating image: " + (data.error || "Unknown error"));
        }
    })
    .catch(error => {
        document.getElementById('loader').style.display = 'none';
        alert("Error: " + error);
    });
}
