document.addEventListener('DOMContentLoaded', function (event) {
    document.querySelector('#vitaminC-form').addEventListener('submit', function(event) {
        let answer = document.querySelector('#vitaminC-answer');
        let feedback = document.querySelector('#vitaminC-feedback');
        if (parseInt(answer.value) === 90) {
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
