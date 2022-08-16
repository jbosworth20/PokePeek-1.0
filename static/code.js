function unhide(class_to_unhide){ /** Make this so it so that there is a class we call and then based on individual ID we determine what is visible */
    var element = document.getElementByClassName(class_to_unhide);
    if(element.style.visibility == "hidden"){
        element.style.visibility = "visible";
    }else{
        element.style.visibility = "hidden";
    }
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


