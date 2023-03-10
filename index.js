// Add a smooth scroll effect to the "About Us" link in the navigation menu
const aboutLink = document.querySelector('a[href="#about"]');

aboutLink.addEventListener('click', (event) => {
  event.preventDefault();
  const aboutSection = document.querySelector('#about');
  aboutSection.scrollIntoView({ behavior: 'smooth' });
});

