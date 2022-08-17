function unhide(id_to_unhide){ /** Make this so it so that there is a class we call and then based on individual ID we determine what is visible */
    var element = document.getElementById(id_to_unhide);
    if(element.style.visibility == "hidden"){
        element.style.visibility = "visible";
    }else{
        element.style.visibility = "hidden";
    }
}



