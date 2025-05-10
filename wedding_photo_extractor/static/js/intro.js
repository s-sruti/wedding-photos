function handleUpload(event) {
  const files = event.target.files;
  const fileNames = Array.from(files).map(file => file.name).join(", ");
  document.getElementById("fileNames").textContent = `Selected: ${fileNames}`;
}

function scrollCarousel(direction) {
  const container = document.getElementById('featureSlider');
  const scrollAmount = 320; // width of a card + margin

  container.scrollBy({
    left: direction * scrollAmount,
    behavior: 'smooth'
  });
}
function submit_it() {
  
 document.getElementById("video_upload").submit();

}


