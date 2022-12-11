function hide(id_to_unhide){ /** Make this so it so that there is a class we call and then based on individual ID we determine what is visible */
    if($(id_to_unhide).is(":visible")){
        $(id_to_unhide).hide();
    }else{
        $(id_to_unhide).show();
    }
}
 
function get_range(element){
    /**  Avg HP: 68, Atk: 75, Avg Def: 73, Avg Sp Atk: 69, Sp Def: 69 Avg Spd: 66 **/
    full_stats_info = document.getElementById(element)
    stat = full_stat_info.replace(/\D/g, '')
    window.alert(stat)
    averages('HP') = 68
    averages('Atk') = 75
    averages('Def') = 73
    averages('SpAtk') = 69
    averages('SpDef') = 69
    averages('Spd') = 66
    /** Know this isn't correct need to get element by id but need  */
    if(stat > averages(element)){
        window.alert("GREEN")
        document.getElementById(element).style.color = "green"
    }else if(stat < averages(element)){
        window.alert("RED")
        document.getElementById(element).style.color = "red"
    }
    
}


