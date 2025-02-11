document.addEventListener('DOMContentLoaded', function () {
    // Check if Payment_Success is equal to 1
    var Payment_Success = 1;

    // Function to open the modal
    function openModal() {
        var modal = document.getElementById('myModal');
        modal.style.display = 'block';

        // Automatically close the modal after 3 seconds
        setTimeout(function () {
            closeModal();
        }, 3000);
    }

    // Function to close the modal
    function closeModal() {
        var modal = document.getElementById('myModal');
        modal.style.display = 'none';
    }

    // Check the condition and open the modal if Payment_Success is equal to 1
    if (Payment_Success === 1) {
        openModal();
    }
});
