function create_types(){ /** Need to think how to use this to determine background color maybe read 
in the text and if = then we choose color? */
    var body = document.getElementsByTagName("body")[0];
    /*Change total_types to size of array containing types*/ 
    var total_types = 1;
    var name_of_type = 'Grass'
    if(total_types = 1){
        var type = document.createElement("button");
        type.innerHTML = name_of_type;
        type.id = name_of_type;
        type.className = 'pokemon_type_single';
        body.insertBefore(type,body.nextSibling);
    }else{
        for(var i = 0;i<total_types;i++){
            var type = document.createElement("button");
            /**button.className = "btn btn-success";**/
            type.innerHTML = 'Nope'; /** This is the label on the button*/
            type.id = name_of_type;
            type.className = 'pokemon_type_dual';
            body.insertBefore(type,body.nextSibling);
        }
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