window.addEventListener("DOMContentLoaded", function() {
    const newsContainer = document.getElementById("container-recipe");
    const newsContent = document.getElementById("news-content");
    const scrollSpeed = 2; // Adjust the scroll speed as needed
  
    function scrollNewsBar() {
      if (newsContainer.scrollLeft >= newsContent.offsetWidth) {
        newsContainer.scrollLeft = 0;
      } else {
        newsContainer.scrollLeft += scrollSpeed;
      }
    }
  
    let animationId;
  
    function startScrolling() {
      animationId = setInterval(scrollNewsBar, 20);
    }
  
    function stopScrolling() {
      clearInterval(animationId);
    }
  
    startScrolling();
  
    // Pause scrolling on mouseover
    newsContainer.addEventListener("mouseover", function() {
      stopScrolling();
    });
  
    // Resume scrolling on mouseout
    newsContainer.addEventListener("mouseout", function() {
      startScrolling();
    });
  });
  