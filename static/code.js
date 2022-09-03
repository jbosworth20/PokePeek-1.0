function unhide(id_to_unhide){ /** Make this so it so that there is a class we call and then based on individual ID we determine what is visible */
    if($(id_to_unhide).is(":visible")){
        $(id_to_unhide).hide();
    }else{
        $(id_to_unhide).show();
    }
}


