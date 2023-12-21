$(document).ready(() => {
  let top = $('.top');
  $('#view-more').click(() => {
    $('html, body').animate({
      scrollTop: $(".thank_you_content").offset().top
    }, 1000);
    $("#create-survey").focus();
  });

//   $('#copy1').click(() => {
//       let copyText = $('#copyInput1').text();
//       // copyText.select();
//       console.log(copyText);
//       document.execCommand("copy", copyText);
//       alert("Text copied to clipboard: " + copyText);
//   });

//   $('#copy2').click(() => {
//     let copyText = document.getElementById("copyInput2");
//     copyText.select();
//     document.execCommand("copy");
//     alert("Text copied to clipboard: " + copyText.value);
// });
});