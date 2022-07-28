function remove_buttons(given_id,needed_amount){
    var parent = document.getElementById(given_id);
    var total_children = parent.childElementCount;
    var amount = total_children - needed_amount;
    for(var i = total_children;i>amount;i--){
        var delete_child = document.getElementById(given_id +"_"+i);
        parent.removeChild(delete_child);
    }
}
function create_types(){ 
    var total_types = 1; /*Change total_types to size of array containing types*/ 
    var type_1 = document.getElementById('type_1');
    var type_2 = document.getElementById('type_2');
    var name_of_type_1 = 'Grass' /*Change this to whatever the element is from the json*/
    type_1.innerHTML = name_of_type_1;
    type_1.id = name_of_type_1;
    if(total_types == 1){
        type_2.remove();
        type_1.classList.remove('pokemon_type_dual');
        type_1.className = 'pokemon_type_single';
    }else{
        var name_of_type_2 = 'Fairy' /*Change this to whatever the element is from the json*/
        type_2.innerHTML =  name_of_type_2;
        type_2.id = name_of_type_2;
    }
}

function create_move_effectiveness(){
    var total_strong = 3;
    var total_weak = 6;
    var total_resist = 0;
}

function create_sliding_list(){
    /*Change 5 to whatever the move set # is from the query*/
    var num_moves = 20;
    for(var i = 0;i<num_moves;i++){
        var move = document.createElement("p");
        var move_name = document.createTextNode("Test??"); /** Replace this with move_name */
        move.append(move_name);
        document.getElementsById("begin").appendChild(move,list);
    }
}
/** For function below was thinking this - go and get move from json that matches the text and from there auto populate */
function show_move(){
    var p = document.createElement
    document.appendChild("p");
    p.innerHTML = "HelloF"
}
function show_tooltext(){

}
function grab_pokemon_name(){
    var pokemon_name = document.getElementById('find_pokemon').value
    alert(pokemon_name)
}