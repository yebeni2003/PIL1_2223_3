// Récupérer tous les boutons ayant la classe "btn-modifier"
var btnsModifier = document.getElementsByClassName('btn-modifier');

// Parcourir tous les boutons et ajouter un gestionnaire d'événement de clic à chacun
for (var i = 0; i < btnsModifier.length; i++) {
  btnsModifier[i].addEventListener('click', function() {
    // Récupérer l'ID de l'emploi à modifier à partir de l'attribut "data-emploi-id"
    var emploiId = this.getAttribute('data-emploi-id');
    window.location.href = '/update_schedule/' + emploiId;

    // Modifier l'action du formulaire pour inclure l'ID de l'emploi
    var form = document.getElementById('updateForm');
    form.action = form.action.replace('0', emploiId);
    
    // Mettre à jour la valeur de l'élément emploiId dans le formulaire
    var emploiIdInput = document.getElementById('emploiId');
    emploiIdInput.value = emploiId;
    
    // Ouvrir le modal de modification
    var modal = document.getElementById('editScheduleModal');
    var modalInstance = new bootstrap.Modal(modal);
    modalInstance.show();
    window.location.href = '/update_schedule/' + emploiId;
  });
}
