document.addEventListener('DOMContentLoaded', function (event) {
    document.querySelector('#vitaminA-form').addEventListener('submit', function(event) {
        let answer = document.querySelector('#vitaminA-answer');
        let feedback = document.querySelector('#vitaminA-feedback');
        if (parseInt(answer.value) === 3000) {
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
