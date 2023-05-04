const images = document.querySelectorAll('.img-container img');
const lightbox = document.createElement('div');
lightbox.className = 'lightbox';
document.body.appendChild(lightbox);

images.forEach((image) => {
  image.addEventListener('click', () => {
    const fullImage = document.createElement('img');
    fullImage.src = image.dataset.image;
    while (lightbox.firstChild) {
      lightbox.removeChild(lightbox.firstChild);
    }
    lightbox.appendChild(fullImage);
    lightbox.style.display = 'flex';
  });
});

lightbox.addEventListener('click', (event) => {
  if (event.target !== event.currentTarget) {
    return;
  }
  lightbox.style.display = 'none';
});

