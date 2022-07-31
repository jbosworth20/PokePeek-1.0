function remove_buttons(given_id,needed_amount){
    var parent = document.getElementById(given_id);
    var total_children = parent.childElementCount;
    for(var i = total_children;i>needed_amount;i--){
        var delete_child = document.getElementById(given_id +"_"+i);
        parent.removeChild(delete_child);

    }
}
function unhide(id_to_unhide){ /** Make this so it so that there is a class we call and then based on individual ID we determine what is visible */
    var element = document.getElementById(id_to_unhide);
    if(element.style.visibility == "hidden"){
        element.style.visibility = "visible";
    }else{
        element.style.visibility = "hidden";
    }
}
function create_types(){ 
    var total_types = 1; /*Change total_types to size of array containing types*/ 
    var type_1 = document.getElementById('pokemon_type_1');
    var type_2 = document.getElementById('pokemon_type_2');
    var name_of_type_1 = 'Grass' /*Change this to whatever the element is from the json*/
    type_1.innerHTML = name_of_type_1;
    type_1.id = name_of_type_1;
    if(total_types == 2){
        var name_of_type_2 = "Fairy" /*Change this to whatever the element is from the json*/
        type_2.innerHTML = name_of_type_2;
        type_2.id = name_of_type_2;
    }else{
        type_2.remove();
    }
}
function create_move_effectiveness(){
    var total_strong = 3;
    var total_weak = 6;
    var total_resist = 0;
    remove_buttons("strong_to",total_strong);
    remove_buttons("weak_to",total_weak);
    remove_buttons("no_effect_to",total_resist);
}
function create_sliding_list(){
    /*Change 5 to whatever the move set # is from the query*/
    var num_moves = 20;
    for(var i = 0;i<num_moves;i++){
        var move = document.createElement("p");
        var move_name = document.createTextNode("Test??"); /** Replace this with move_name */
        move.append(move_name);
        document.getElementsById("scrollbox").appendChild(move,list);
    }
}
/** Was thinking you auto populate item in list in scrollbox and pull info from name alone*/
/** Need to get move info from move on power and pp */
function show_move(){
    document.getElementById('move_section').style.visibility = "visible";
    document.getElementById('move_label').innerHTML = "Razorleaf"
    document.getElementById('move_info').innerHTML = "Sharp-edged leaves are launched to slash at opposing Pokémon. Critical hits land more easily."
}
function show_tooltext(){

}
function grab_pokemon_name(){
    var pokemon_name = document.getElementById('search_pokemon').value
    alert(pokemon_name)
}