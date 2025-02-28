document.addEventListener("DOMContentLoaded", function() {
    const tasks = document.querySelectorAll(".task");
    const columns = document.querySelectorAll(".dashboard__section");

    tasks.forEach(task => {
        task.addEventListener("dragstart", () => {
            task.classList.add("dragging");
        });

        task.addEventListener("dragend", () => {
            task.classList.remove("dragging");
        });
    });

    columns.forEach(column => {
        column.addEventListener("dragover", (e) => {
            e.preventDefault();
            column.classList.add("dragover");
            const draggingTask = document.querySelector(".dragging");
            column.appendChild(draggingTask);
        });

        column.addEventListener("dragleave", () => {
            column.classList.remove("dragover");
        });

        column.addEventListener("drop", () => {
            column.classList.remove("dragover");
        });
    });
});
