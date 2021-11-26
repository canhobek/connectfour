document.addEventListener('DOMContentLoaded', function() {
   const xhttp = new XMLHttpRequest();
   document.querySelectorAll('button').forEach(function(button) {
       button.onclick = function() {
           const col = button.dataset.col;
           xhttp.open("GET", "/play/" + col, true);
           xhttp.send();
           window.location.reload();
       }
   });
});
