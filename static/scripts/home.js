var search = document.getElementById('search');


function search_cards() {
    var cards = document.getElementsByClassName('card');
    var hiddenCards = document.getElementsByClassName("hidden");
    var filter = search.value.toLowerCase();
    for (i=0; i < cards.length; i++) {
        if (cards[i].innerText.toLowerCase().includes(filter)) {
            cards[i].style.display = "block";
        } else {
            cards[i].style.display = "none";
        }
    };
};


search.addEventListener('keyup', search_cards);


            // cards[i].style.opacity = "1";
            // cards[i].style.height = "30vh";
            // cards[i].addEventListener("transitionend", function() {
            //     this.classList.remove("hidden");
            // });
