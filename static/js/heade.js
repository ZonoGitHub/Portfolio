const livretohover = document.querySelector('.nav-livres');
const livretodisplay = document.querySelector('.tohide1');
const toblack = document.querySelector('.toblackonclick')
    livretohover.addEventListener("mouseover", function(){
        livretodisplay.style.display = 'block';
        toblack.style.backgroundColor = 'white';
          

       /*  document.addEventListener('mouseover', function (e) {
            // Vérifier si l'élément cliqué n'est pas le bouton ou l'élément à afficher
                 if (e.target !== livretohover && e.target !== livretodisplay) {
                      // Masquer l'élément
                      livretodisplay.style.display = 'none';
                  }
      });  */
    });
     livretohover.addEventListener("mouseout", function(){
        livretodisplay.style.display = 'none';
        toblack.style.backgroundColor = '#212c3f';
       });
    livretodisplay.addEventListener("mouseover", function(){
        toblack.style.backgroundColor = 'white';
        livretodisplay.style.display = 'block';
    }) ;


   

const ebooktohover = document.querySelector('.nav-ebooks');
const ebooktodisplay = document.getElementById('menu-ebooks');
const toblack1 = document.querySelector('.toblackonclick1')
    ebooktohover.addEventListener("mouseover", function(){
        ebooktodisplay.style.display = 'block';
        toblack1.style.backgroundColor = 'white';
    });
    ebooktohover.addEventListener("mouseout", function(){
        ebooktodisplay.style.display = 'none';
        toblack1.style.backgroundColor = '#212c3f';

       });
       ebooktohover.addEventListener("mouseover", function(){
        toblack1.style.backgroundColor = 'white';
        ebooktodisplay.style.display = 'block';
    }) ;


/* const content_20 = document.querySelector('.content_20')
const section_row = document.querySelector('.submenu-section-row');
 */const nouveaute = document.querySelector('.nav-livres-preferes-des-libraires');
const nouveautetodisplay = document.getElementById('menu-livres-preferes-des-libraires');
const toblack2 = document.querySelector('.toblackonclick2')

nouveaute.addEventListener("mouseover", function(){
    nouveautetodisplay.style.display = 'block';
    toblack2.style.backgroundColor = 'white';
   
    }); 
    nouveaute.addEventListener("mouseout", function(){
        nouveautetodisplay.style.display = 'none';
        toblack2.style.backgroundColor = '#212c3f';
       });
       nouveautetodisplay.addEventListener("mouseover", function(){
        nouveautetodisplay.style.display = 'block';
        toblack2.style.backgroundColor = 'white';

       });


const prix_reduits = document.querySelector('.nav-livres-a-prix-reduits');
const prix_reduitstodisplay = document.getElementById('menu-livres-a-prix-reduits');
const toblack3 = document.querySelector('.toblackonclick3');
prix_reduits.addEventListener("mouseover", function(){
    prix_reduitstodisplay.style.display = 'block';
    toblack3.style.backgroundColor = 'white';
    });
    prix_reduits.addEventListener("mouseout", function(){
        prix_reduitstodisplay.style.display = 'none';
        toblack3.style.backgroundColor = '#212c3f';
       });
    prix_reduitstodisplay.addEventListener("mouseover", function(){
    prix_reduitstodisplay.style.display = 'block';
    toblack3.style.backgroundColor = 'white';
    });
   

const bonplan = document.querySelector('.nav-bons-plans-livres');
    bonplan.addEventListener("mouseover", function(){
   // bonplantodisplay.style.display = 'block';
         });/*
        bonplan.addEventListener("mouseout", function(){
        bonplantodisplay.style.display = 'none';
        }); */

const jeuxetjouet = document.querySelector('.nav-jeux-et-jouet');
const jeuxetjouettodisplay = document.getElementById('menu-jeux-et-jouet');
const toblack4 = document.querySelector('.toblackonclick4');
    jeuxetjouet.addEventListener("mouseover", function(){
    jeuxetjouettodisplay.style.display = 'block';
    toblack4.style.backgroundColor = 'white';
        });
        jeuxetjouet.addEventListener("mouseout", function(){
        jeuxetjouettodisplay.style.display = 'none';
        toblack4.style.backgroundColor = '#212c3f';
        });
        jeuxetjouettodisplay.addEventListener("mouseover", function(){
            jeuxetjouettodisplay.style.display = 'block';
            toblack4.style.backgroundColor = 'white';
                });