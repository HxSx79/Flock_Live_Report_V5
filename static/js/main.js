// Add close application function
function closeApplication() {
    if (confirm('Are you sure you want to close the application?')) {
        fetch('/shutdown', { method: 'POST' })
            .then(() => window.close())
            .catch(() => window.close());
    }
}