function generateLyrics() {
    var seedText = document.getElementById("seedText").value;
    var nextWords = parseInt(document.getElementById("nextWords").value);
    
    fetch('/generate_lyrics', {
        method: 'POST',
        body: new URLSearchParams({ seedText: seedText, nextWords: nextWords }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
    .then(response => response.text())  // Modify this based on your response format
    .then(data => {
        // Display the generated lyrics on the page
        var resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = data;
    })
    .catch(error => console.error(error));
}
