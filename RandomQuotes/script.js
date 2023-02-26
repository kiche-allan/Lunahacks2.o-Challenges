
// Get references to the quote and author elements in the HTML document
const quote = document.getElementById("quote");
const author = document.getElementById("author");

// Define the URL of the API that will be used to fetch the quote
const api_url = "https://api.quotable.io/random";

// Get a reference to the button element in the HTML document
const button = document.getElementById('button');

/**
 * Fetches a random quote from the specified URL and updates the quote and author elements in the HTML document with the retrieved data.
 *
 * @param {string} url The URL of the API to fetch the quote from.
 * @returns {Promise} A Promise that resolves with the retrieved quote data.
 */
async function getquote(url){
    // Use the fetch API to send a GET request to the specified URL and wait for the response
    const response = await fetch(url);

    // Parse the response as JSON and wait for the result
    var data = await response.json();

    // Log the retrieved data to the console for debugging purposes
    console.log(data)

    // Update the quote and author elements in the HTML document with the retrieved data
    quote.innerHTML = data.content;
    author.innerHTML = data.author;
};

// Attach an event listener to the button element that calls the getquote function when the button is clicked
button.addEventListener('click', () => {
    getquote(api_url);
})