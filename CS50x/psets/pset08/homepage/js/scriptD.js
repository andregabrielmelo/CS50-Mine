document.addEventListener('DOMContentLoaded', function (event) {
    document.querySelector('#vitaminD-form').addEventListener('submit', function(event) {
        let answer = document.querySelector('#vitaminD-answer');
        let feedback = document.querySelector('#vitaminD-feedback');
        if (parseInt(answer.value) === 600) {
            feedback.innerHTML = 'Correct';
            answer.style.backgroundColor = '#50C878';
        }
        else {
            feedback.innerHTML = 'Incorrect';
            answer.style.backgroundColor = '#f1807e';
        }
        event.preventDefault();
    });
});
