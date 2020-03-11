const translations = {
  "Click on 'Create a new sandbox' to create an isolated instance to hack.":
    "Klik op 'Maak een nieuwe sandbox' om een nieuwe, geisoleerde instantie op te starten."
};

const language = localStorage.getItem("workshop-language") || "english";

export const translate = sentence => {
  if (translations[sentence]) return translations[sentence];
  return "GEEN VERTALING";
};

export const translateDirective = {
  // When the bound element is inserted into the DOM...
  bind(el) {
    // Focus the element
    if (language == "dutch") el.innerHTML = translate(el.innerHTML);
  }
};
