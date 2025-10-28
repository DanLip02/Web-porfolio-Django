// Раскрытие проектов при клике на категорию
document.querySelectorAll('.category').forEach(cat => {
    cat.addEventListener('click', () => {
        const projectsList = cat.nextElementSibling;
        if (projectsList) {
            projectsList.style.display = (projectsList.style.display === 'block') ? 'none' : 'block';
        }
    });
});

// Раскрытие popup проекта
document.querySelectorAll('.project-title').forEach(title => {
    title.addEventListener('click', () => {
        const popup = title.nextElementSibling;
        if (popup) {
            popup.style.display = (popup.style.display === 'block') ? 'none' : 'block';
        }
    });
});
