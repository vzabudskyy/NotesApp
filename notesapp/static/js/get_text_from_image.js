function gettextfromimage(form_id){
    const XHR = new XMLHttpRequest();
    const form = document.getElementById(form_id);
    const FD = new FormData(form);
    var http = new XMLHttpRequest();
    http.open("POST", "http://127.0.0.1:8000/notesapp/gettextfromimage/", false);
    http.send(FD);
    if (http.status == 200)
    {
        document.getElementById('id_text').value = http.responseText;
    }
    else
    {
        alert("Ooops, something went wrong... (Status: ${http.status})");
    }
};