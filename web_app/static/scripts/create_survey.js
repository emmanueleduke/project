$(document).ready(() => {

  let count = 1;

  $('#add-questions').click(() => {
    let questionId = `Question-${count}`;
    const input = `${questionId}-input`;
    const placeholder = `question: What is the question?\nchoices: [choice1, choice2, choice3, choice4]\nor\ntextbox: placeholder.`;
    $(`
    <label> ${questionId} </label><br>
    <input type="text" name=${questionId} class=${questionId} id=question-box placeholder="${placeholder}"><br><br>
    `).appendTo('.questions');
    count++;
  });
});

/* 
<label>Question</label><br>
<input type="text" name="question1" id="survey-question" placeholder="Question"><br><br>
<input type="button" id="add-box" value="Add Input box"><br>
<input type="button" id="add-options" value="Add options"><br><br>
*/