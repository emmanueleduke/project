$(document).ready(() => {

  let count = 1;


  // Add questions
  $('#add-questions').click(() => {
    let questionId = `Question-${count}`;
    let label = `Question ${count}`;
    const input = `${questionId}-input`;
    const placeholder = `question: What is the question?\nchoices: ['choice1', 'choice2', 'choice3', 'choice4']\nor\nchoices: None (for textbox).`;

    $('#add-questions').before(`
    <div class="questions" id=${questionId}>
      <label> ${label} </label>
      <textarea name=${questionId} cols="50" rows="5" placeholder="${placeholder}"></textarea>
    </div>
    `);
    count++;
    console.log(questionId);
  });


  // Remove the questions
  $('#remove-questions').click(() => {
    if (count >= 2) {
      count--;
    } else {
      count = 1;
    }
  
    let questionId = `#Question-${count}`;
    console.log(questionId);
    $(questionId).remove();
  });


  // Banner slider
  $('.banner_left').click(() => {
    $(".banner").animate({ height: '5vh' }, 1000);
    $(".banner_left").animate({ opacity: 0 }, 1000);
    $(".banner_right").animate({ opacity: 0 }, 1000);
    $("#survey_title").trigger("focus");
  });
});

//     <input type="text" name=${questionId} class=${questionId} id=question-box placeholder="${placeholder}"><br><br>
