/* const bouton = document.getElementById("telecharge");
        // Ajoutez un gestionnaire d'événements au bouton
    bouton.addEventListener("click", function() {
       var value=document.getElementById('telechare').value
       /* $.ajax({
        type: "GET",
        url: "/livre/compteur/" ,  // L'URL de la vue Django
        /*data: {
            csrfmiddlewaretoken: '{{ csrf_token }}', // Token CSRF de Django
            
        },*//*
        success: function(data) {
            alert(data.message); // Affiche la réponse du serveur
        },
        error: function(error) {
            alert(error);
        }
    });
        
       alert(value);
       alert('bonjour');
        
});
*/


const dropdown = document.querySelector(".dropdown");
const dropdown_content = document.querySelector(".dropdown-content")
dropdown.addEventListener("click", function() {
       if( dropdown_content.style.display =='block')
           dropdown_content.style.display='none';
        else
           dropdown_content.style.display='block';
    
    // Ajouter un gestionnaire d'événement au clic n'importe où sur la page
    document.addEventListener('click', function (e) {
        // Vérifier si l'élément cliqué n'est pas le bouton ou l'élément à afficher
             if (e.target !== dropdown && e.target !== dropdown_content) {
                  // Masquer l'élément
                  dropdown_content.style.display = 'none';
              }
  
  }); 
}); 

/*dropdown.addEventListener("mouseout", function() {
    var dropdown_content = document.querySelector(".dropdown-content")
    dropdown_content.style.display='none';
}); */


const not = document.getElementById("notification");
const notifi = document.querySelector(".glostick1");
not.addEventListener("click", function() {
   
      if( notifi.style.display =='block')
           notifi.style.display='none';
        else
           notifi.style.display='block';

         // Ajouter un gestionnaire d'événement au clic n'importe où sur la page
         document.addEventListener('click', function (e) {
          // Vérifier si l'élément cliqué n'est pas le bouton ou l'élément à afficher
               if (e.target !== not && e.target !== notifi) {
                    // Masquer l'élément
                    notifi.style.display = 'none';
                }
    
    }); 
});




/* Toast */

/* const bouton = document.getElementsByClassName('telecharge');
  bouton.forEach(bouton => {
    bouton.classList.add('telecherge');
});   
const toastBox = document.getElementById('toastBox');
const msg = '<i class="fa-solid fa-circle-check"></i> Félicitation! Téléchargement Reussi !';
bouton.addEventListener('click', function(){
   /*  let toast = document.createElement('div');
        toast.classList.add('toast');
        toast.innerHTML = msg;
        toastBox.appendChild(toast);  *
        toastBox.style.backgroundColor ="white";
        toastBox.innerHTML = msg;
        toastBox.style.display ='block' 

        setTimeout(()=>{
        toastBox.remove();
        },6000);  
       
}); */

const bouton = document.querySelector('.telecharge');
const toastBox = document.getElementById('toastBox');
const msg = '<i class="fa-solid fa-circle-check"></i> Félicitation! Téléchargement Reussi !';
 function toaster(){
   /*  let toast = document.createElement('div');
        toast.classList.add('toast');
        toast.innerHTML = msg;
        toastBox.appendChild(toast);  */
        toastBox.style.backgroundColor ="white";
        toastBox.innerHTML = msg;
        toastBox.style.display ='block' 
        //window.location.reload();

        setTimeout(()=>{
        toastBox.remove();
        },6000);  
       
    };


/* command = document.getElementById('commanderBook');
command.addEventListener('click', function() {
    var confirmation = confirm("Voulez-vous vraiment passer cette commande ?");
    if (confirmation) {
        // Si l'utilisateur clique sur "OK"
        // Vous pouvez ajouter ici le code à exécuter lorsque la commande est confirmée
        alert("Commande confirmée !");
    } else {
        // Si l'utilisateur clique sur "Annuler"
        // Vous pouvez ajouter ici le code à exécuter lorsque la commande est annulée
        alert("Commande annulée.");
    }
    //alert('ok');
}); */




  
  

   
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Vérifier si le cookie correspond au nom du jeton CSRF
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');
    

    //document.getElementById('commanderBook').addEventListener('click', function() {
        // Affichage de la fenêtre modale au centre de l'écran

function commander(livre_id){
        document.getElementById('confirmationModal').style.display = 'block';
     // });

      document.getElementById('cancelButton').addEventListener('click', function() {
        // Cacher la fenêtre modale si l'utilisateur clique sur "Annuler"
        document.getElementById('confirmationModal').style.display = 'none';
      });
      
      document.getElementById('confirmButton').addEventListener('click', function() {
     
     $.ajax({
        type: "POST",
        url: "/livre/creer_commande/"+ livre_id+"/" ,  // L'URL de la vue Django
        headers: { "X-CSRFToken": csrftoken },
        data: {
            livre_id: 1,  // ID du livre que vous souhaitez commander
        },
         success: function() {
            document.getElementById('felicitaioncommande').style.display = 'block';

            document.getElementById('cancelfelicit').addEventListener('click', function() {
                document.getElementById('felicitaioncommande').style.display = 'none';
            });

            setTimeout(()=>{
                document.getElementById('felicitaioncommande').style.display = 'none';
                },4000);  
        },
         error: function(error) {
            alert('Erreur ! Votre commande n\'a pas etet effectuer ceuillez reessayez SVP !');
        }  
    });
    
    
    document.getElementById('confirmationModal').style.display = 'none';
  });
}


const commspec = document.getElementById('commandespeciale');
const commandespecil = document.getElementById('commandespecil');
commandespecil.addEventListener('click', function() {
    commspec.style.display ='block' ;
   });
   document.getElementById('Annulespeciale').addEventListener('click', function() {
    commspec.style.display ='none' ;
   });
   document.getElementById('close').addEventListener('click', function() {
    commspec.style.display ='none' ;
   });