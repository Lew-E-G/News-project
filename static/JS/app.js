// const observer = new IntersectionObserver((entries) => {
//     entries.forEach((entry) => {
//         console.log(entry)
//         if (entry.isIntersecting) {
//             entry.target.classList.add('show');
//         } else {
//             entry.target.classList.remove('show');
//         }
//     });
// });

// const hiddenElements = document.querySelectorAll('.hidden')
// hiddenElements.forEach((el) => observer.observe(el));

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.remove('show'); // Remove class to reset animation
            void entry.target.offsetWidth; // Trigger reflow to ensure the animation resets
            entry.target.classList.add('show'); // Add class to start the animation
        } else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));