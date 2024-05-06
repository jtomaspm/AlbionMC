function insertParagraph() {
    const testDiv = document.getElementById("test");
    if (testDiv) {
        const p = document.createElement("p");
        p.textContent = "The js import from html is working!";
        testDiv.appendChild(p);
    } else {
        console.error("Div with id 'test' not found.");
    }
}

insertParagraph();