document.addEventListener('DOMContentLoaded', function() {
   document.querySelectorAll('button').forEach(function(button) {
       button.onclick = function() {
           alert(button.dataset.col);
       }
   });
});
