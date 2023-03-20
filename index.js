// Add a hover effect to the Learn More button
	const learnMoreBtn = document.querySelector('.button');
	learnMoreBtn.addEventListener('mouseover', function() {
		  learnMoreBtn.style.backgroundColor = '#3E8E41';
	});
learnMoreBtn.addEventListener('mouseout', function() {
	  learnMoreBtn.style.backgroundColor = '#4CAF50';
});

