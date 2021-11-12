document.addEventListener('DOMContentLoaded', function() {
    const xhttp = new XMLHttpRequest();
   document.querySelectorAll('button').forEach(function(button) {
       button.onclick = function() {
           const xhttp = new XMLHttpRequest();
           const col = button.dataset.col;
           xhttp.open("GET", "/play/" + col, true);
           xhttp.send();
           window.location.reload();
       }
   });

   /*xhttp.addEventListener("load", (reponse) -> {
     xhttp.open("GET", "/");
     xhttp.send();
   });*/
});
