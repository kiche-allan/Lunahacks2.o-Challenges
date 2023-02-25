const quotes = [
    {
      text: "Be the change you want to see in the world.",
      author: "Mahatma Gandhi"
    },
    {
      text: "It does not matter how slowly you go as long as you do not stop.",
      author: "Confucius"
    },
    {
      text: "Believe you can and you're halfway there.",
      author: "Theodore Roosevelt"
    },
    {
      text: "Strive not to be a success, but rather to be of value.",
      author: "Albert Einstein"
    },
    {
      text: "The only way to do great work is to love what you do.",
      author: "Steve Jobs"
    }
  ];
  
  const quoteText = document.querySelector("#text");
  const quoteAuthor = document.querySelector("#author");
  const newQuoteBtn = document.querySelector("#new-quote");
  
  function getRandomQuote() {
    return quotes[Math.floor(Math.random() * quotes.length)];
  }
  
  function renderQuote() {
    const quote = getRandomQuote();
    quoteText.textContent = quote.text;
    quoteAuthor.textContent = `- ${quote.author}`;
  }
  
  newQuoteBtn.addEventListener("click", renderQuote);
  
  renderQuote();
  