window.copyText = function(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";  // Prevent scrolling to bottom of page in MS Edge.
    textArea.style.top = "0"; // Move element out of screen
    textArea.style.left = "0"; // Move element out of screen
    textArea.style.opacity = "0"; // Move element out of screen

    document.body.appendChild(textArea);

    textArea.focus();
    textArea.select();

    try {
        const successful = document.execCommand('copy');
        return successful;
    } catch (err) {
        return false;
    } finally {
        document.body.removeChild(textArea);
    }
};



 async  Task Copytitle()
 {
     await JS.InvokeVoidAsync("copyText", Title);
 }