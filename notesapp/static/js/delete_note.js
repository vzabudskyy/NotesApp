function delete_note(link, csrftoken){
    const response = fetch(link, {
            method: 'DELETE',
            headers: {
                "X-CSRFToken": csrftoken,
            }
        });
    location.reload()
};