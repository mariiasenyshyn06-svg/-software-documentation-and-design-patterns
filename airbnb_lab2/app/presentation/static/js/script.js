function openModal(id) {
    document.getElementById(id).style.display = 'block';
}

function closeModal(id) {
    document.getElementById(id).style.display = 'none';
}

window.onclick = function(event) {
    document.querySelectorAll('.modal').forEach(m => {
        if (event.target === m) m.style.display = "none";
    });
}

function confirmDelete() {
    return confirm("Ви точно хочете видалити цей запис?");
}