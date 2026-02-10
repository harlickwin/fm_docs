// Formula Copy Functionality
// Adds copy-to-clipboard functionality for formula code blocks

document.addEventListener('DOMContentLoaded', function() {
    // Find all copy buttons
    const copyButtons = document.querySelectorAll('.copy-btn');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the text to copy from data-copy attribute
            const textToCopy = this.getAttribute('data-copy');
            
            if (!textToCopy) {
                console.warn('No data-copy attribute found on button');
                return;
            }
            
            // Use the Clipboard API to copy text
            navigator.clipboard.writeText(textToCopy).then(() => {
                // Success feedback
                const originalText = this.textContent;
                this.textContent = 'Copied!';
                this.style.background = '#10b981'; // Success green
                
                // Reset button after 2 seconds
                setTimeout(() => {
                    this.textContent = originalText;
                    this.style.background = ''; // Reset to CSS default
                }, 2000);
            }).catch(err => {
                // Error feedback
                console.error('Failed to copy text: ', err);
                const originalText = this.textContent;
                this.textContent = 'Failed';
                this.style.background = '#ef4444'; // Error red
                
                // Reset button after 2 seconds
                setTimeout(() => {
                    this.textContent = originalText;
                    this.style.background = ''; // Reset to CSS default
                }, 2000);
            });
        });
    });
    
    // Log initialization
    console.log(`Formula copy functionality initialized for ${copyButtons.length} buttons`);
});
