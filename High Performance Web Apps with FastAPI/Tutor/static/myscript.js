const myFunction = () => {
    let text;
    if(confirm("Do you want to Continue\nChoose Ok/Cancel") == true) {
        text = "You pressed OK!";
    }else{
        text = "You pressed Cancel";
    }
    document.getElementById("response").innerHTML = text;
}