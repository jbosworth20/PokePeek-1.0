function create_types(){ 
    var total_types = 1; /*Change total_types to size of array containing types*/ 
    var type_1 = document.getElementById('type_1');
    var type_2 = document.getElementById('type_2');
    /** We know we are going to need to set the first type since all pokemon have at least one type */
    var name_of_type_1 = 'Grass' /*Change this to whatever the element is from the json*/
    type_1.innerHTML = name_of_type_1;
    type_1.id = name_of_type_1;
    if(total_types == 1){
        type_2.remove();
        type_1.classList.remove('pokemon_type_dual');
        type_1.className = 'pokemon_type_single';
    }else{
        var name_of_type_2 = 'Grass'
        type_2.innerHTML =  name_of_type_2;
        type_2.id = name_of_type_2;
    }
}


function create_accordion(){
    /*Change 5 to whatever the move set # is from the query*/
    var list = document.getElementsById("pokemon_moves");
    for(var i = 0;i<5;i++){
        var move = document.createElement("li");
        move.id = 'accordion';
        move.appendChild(document.createTextNode("Tackle")); /** This is the label on the button*/
        document.querySelector('ul').appendChild(move);
        alert(move);
    }
    alert(move);
}

function show_tooltext(){

}
function grab_pokemon_name(){
    var pokemon_name = document.getElementById('find_pokemon').value
    alert(pokemon_name)
}