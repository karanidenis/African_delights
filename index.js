var learnmoreButton = document.getElementById("learn-more-button");
var learnmoreSection = document.getElementById("learn-more-section");

learnmoreButton.addEventListener("click", function() {
  learnmoreSection.style.display = "block";
  window.scrollTo(0,document.body.scrollHeight);
});

