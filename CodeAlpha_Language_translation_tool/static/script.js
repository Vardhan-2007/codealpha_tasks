function translateText() {
  const text = document.getElementById("inputText").value.trim();
  const sourceLang = document.getElementById("sourceLang").value;
  const targetLang = document.getElementById("targetLang").value;
  const output = document.getElementById("output");

  if (!text) {
    output.innerText = "Please enter some text to translate.";
    return;
  }

  output.innerText = "Translating...";

  fetch("/translate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text: text,
      source: sourceLang,
      target: targetLang
    })
  })
    .then(response => response.json())
    .then(data => {
      output.innerText = data.translated;
    })
    .catch(error => {
      output.innerText = "Error: Could not translate. Try again.";
      console.error(error);
    });
}
function copyText() {
  const output = document.getElementById("output").innerText;
  if (!output) return;
  navigator.clipboard.writeText(output)
    .then(() => alert("Copied to clipboard!"))
    .catch(err => console.error("Copy failed:", err));
}

function speakText() {
  const output = document.getElementById("output").innerText;
  if (!output || output === "Translation will appear here...") return;

  const targetLang = document.getElementById("targetLang").value;
  const voices = speechSynthesis.getVoices();

  const matchingVoice = voices.find(v => v.lang.toLowerCase().startsWith(targetLang.toLowerCase()));

  if (!matchingVoice) {
    alert("Sorry, text-to-speech for this language isn't available in your browser.");
    return;
  }

  const utterance = new SpeechSynthesisUtterance(output);
  utterance.voice = matchingVoice;
  utterance.lang = matchingVoice.lang;
  speechSynthesis.speak(utterance);
}
function swapLanguages() {
  const source = document.getElementById("sourceLang");
  const target = document.getElementById("targetLang");
  const temp = source.value;
  source.value = target.value;
  target.value = temp;
}