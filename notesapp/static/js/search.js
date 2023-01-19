function searchtext(text, link, csrf_token) {
    const XHR = new XMLHttpRequest();
    var http = new XMLHttpRequest();
    http.open("GET", link + "?search=" + text, false);
    http.send('');
    var parsed = JSON.parse(http.response);
    var mlt = ``;
    for (var i=0; i<parsed.length; i++){
        var title = parsed[i].fields.title;
        var category = parsed[i].fields.category;
        var reminder = parsed[i].fields.reminder;
        var text = parsed[i].fields.text;
        var id = parsed[i].pk;
        mlt += `
            <div class="note" onLoad="pickColor()">
                <div class="buttonalignment">
                    <button class="actionbutton" value="${id}" onclick="play(this.value, '/notesapp/getaudio/');">
                        <span class="deletebutton">&#x1F508;</span>
                    </button>
                    <button class="actionbutton" onclick="window.location.href='/notesapp/usernote/${id}/';">
                        <span class="updatebutton">&#x270E;</span>
                    </button>
                    <button class="actionbutton" onclick="delete_note('/notesapp/usernote/${id}/', '${csrf_token}');">
                        <span class="deletebutton">&#x2715;</span>
                    </button>
                </div>
            Title: ${title}<br>
            Category: ${category}<br>
            Reminder: ${reminder}<br><br>
            ${text}
            </div>`
    }
    document.getElementsByClassName('main')[0].innerHTML = mlt;
}