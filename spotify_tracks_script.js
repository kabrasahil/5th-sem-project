function findSpotifyTracks() {
    var genre = document.getElementById("genre").value;
    var maxListeners = parseInt(document.getElementById("maxListeners").value);
    
    fetch('/find_spotify_tracks', {
        method: 'POST',
        body: new URLSearchParams({ genre: genre, maxListeners: maxListeners }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
    .then(response => response.text())  // Modify this based on your response format
    .then(data => {
        // Display the Spotify tracks on the page
        var resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = data;
    })
    .catch(error => console.error(error));
}
