function play(id, link) {
    new Audio(link + "?sound_note=" + id).play();
}
