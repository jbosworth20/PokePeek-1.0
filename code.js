function create_types(){
    var body = document.getElementsByTagName("body")[0]
    /*Change 5 to whatever the type # is from the query*/
    for(var i = 0;i<1;i++){
        var button = document.createElement("button")
        button.className = "btn btn-light"
        button.innerHTML = 'grass' /** This is the label on the button*/
}

function create_accordion(){
    /*Change 5 to whatever the move set # is from the query*/
    var body = document.getElementsByTagName("body")[0]
    var start = document.getElementById('start')
    for(var i = 0;i<5;i++){
        var button = document.createElement("button")
        button.id = 'accordion'
        button.className = "btn btn-light"
        button.innerHTML = 'tackle' /** This is the label on the button*/
        start.parentNode.insertBefore(button,start)
        body.appendChild(button)
    }
}

function show_tooltext(){

}
function grab_pokemon_name(){
    var pokemon_name = document.getElementById('find_pokemon').value
    alert(pokemon_name)
}