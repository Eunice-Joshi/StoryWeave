const apiKey = "tgp_v1_4NWwD3gCLsrp6r-xB4-3S5BCUu1ZYkpsOi0l445OJOQ"; 
const apiUrl = "http://127.0.0.1:5000/generate";

document.getElementById("generateBtn").addEventListener("click", async function () {
    const genre = document.getElementById("genre").value;
    const keywords = document.getElementById("keywords").value.trim();
    const wordcount = document.getElementById("wordcount").value;
    
    let prompt = `Write a ${genre} story with approximately ${wordcount} words.`;
    if (keywords) {
        prompt += ` Include the following elements: ${keywords}.`;
    }

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        document.getElementById("storyOutput").innerText = data.story;
    } catch (error) {
        document.getElementById("storyOutput").innerText = "Error generating story. Try again!";
    }
});

function updateWordCount() {
    document.getElementById("wordcount-display").innerText = document.getElementById("wordcount").value + " words";
}
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        document.getElementById("splash").style.display = "none";
    }, 3000); // Hides splash after 3 seconds
});
