// ADDS IMAGE PREVIEW TO ADD RECIPE FORM

var fileBtn = document.getElementById("fileBtn");
var fileUpload = document.getElementById("fileUpload")


function preview() {
    document.getElementById('fileUpload').click();
}

function showPreview() {
    fileBtn.style.background = 'url(' + window.URL.createObjectURL(this.files[0]) + ')';
    fileBtn.style.backgroundSize = 'contain';
    fileBtn.value = '';
}


fileBtn.addEventListener("click", preview)
fileUpload.addEventListener("change", showPreview)
