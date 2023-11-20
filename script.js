function searchSongs() {
    var inputLyrics = document.getElementById("lyricsInput").value;
    fetch('/search', {
        method: 'POST',
        body: JSON.stringify({ lyricsInput: inputLyrics }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        var resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = '';  // Clear previous results
        data.forEach(function(song, index) {
            resultsDiv.innerHTML += <p>${index + 1}. Song: ${song[0]}, Artist: ${song[1]}, Levenshtein Distance: ${song[2]}</p>;
        });
    })
    .catch(error => console.error(error));
}