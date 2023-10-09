/**
 * @Class       : main
 * @Author      : Darwin Neira Carrasco
 * @Email       : dneirac@unsa.edu.pe
 * @Description : main
 */


// Configuración del mapa de Mapbox
mapboxgl.accessToken = 'pk.eyJ1IjoiamlubmJpdCIsImEiOiJjbG5na21ycnYwNTNkMm1xbHZpdmpoM3A3In0.zrDQjfODs32fdfuY-PWtaQ';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
  
    center: [36.998944, -36.538333], // Coordenadas del marcador
    zoom: 14 // Nivel de zoom
});

// Marcador en el mapa
var marker = new mapboxgl.Marker()
    .setLngLat([36.998944, -36.538333]) // Coordenadas del marcador
    .addTo(map);

// Obtiene el modal
var modal = document.getElementById("myModal");
console.log("modal" + modal)

// Cuando el usuario hace clic en el marcador, abre el modal 
marker.getElement().addEventListener('click', function() {
    console.log("eventomaker")
    modal.style.display = "block";
    modal.classList.add("show"); // Agrega la clase "show" para activar la animación de entrada

    console.log("despuesdeshow")
});

// Cuando el usuario hace clic en <span> (x) o el botón "Cerrar", cierra el modal
var closeButtons = document.querySelectorAll(".close, .modal-footer button[data-dismiss='modal']");
for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].onclick = function() {
        modal.style.display = "none";
        modal.classList.remove("show"); // Elimina la clase "show" para activar la animación de salida
    }
}

// Inicializa Perfect Scrollbar en el contenido del modal
//var ps = new PerfectScrollbar(".modal-body-scroll");

// Obtener todas las etiquetas de estrellas
var starLabels = document.querySelectorAll('.rating label');

// Agregar evento de clic a las etiquetas de estrellas
starLabels.forEach(function(label, index) {
    label.addEventListener('click', function() {
        // Limpiar todas las estrellas previamente pintadas de amarillo
        starLabels.forEach(function(starLabel, starIndex) {
            if (starIndex <= index) {
                starLabel.style.color = '#FFD700'; // Amarillo más intenso
            } else {
                starLabel.style.color = '#ddd';
            }
        });
    });
});

