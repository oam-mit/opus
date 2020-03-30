var outputArea = $("#chat-output");
  
$("#user-input-form").on("submit", function(e) {
  
  e.preventDefault();
  
  var message = $("#user-input").val();
  
  outputArea.append(`
    <div class='bot-message'>
      <div class='message'>
        You:  ${message}
      </div>
    </div>
  `);

  $.ajax({

    type:'GET',
    url:"/bot_reply",
    data:{
        'mes':message
    },
    success:function(response)
    {
        outputArea.append(`
      <div class='user-message'>
        <div class='message'>
          BOT:  ${response}
        </div>
      </div>
    `);

    }

});
  
  $("#user-input").val("");
  
});

function hidefunction()
{
  document.getElementById("chatting_id").style.display="none";
}
function showfunction()
{
  document.getElementById("chatting_id").style.display="block";
}