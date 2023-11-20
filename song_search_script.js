function searchSongs() {
    var inputLyrics = document.getElementById("lyricsInput").value;
    fetch('/search_song', {
        method: 'POST',
        body: new URLSearchParams({ lyricsInput: inputLyrics }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
    .then(response => response.text())  // Modify this based on your response format
    .then(data => {
        // Display the results on the page
        var resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = data;
    })
    .catch(error => console.error(error));
}
