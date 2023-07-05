let current_state = "offer_type";
let previous_answers = {};

$(document).ready(function() {
    $('#userInputForm').on('submit', function(e) {
        e.preventDefault();

        let userText = $('#userInput').val();
        $('#chatbox').append('<div class="messageContainer"><p class="userMessage">User: ' + userText + '</p></div>');
        $('#userInput').val("");
        $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);

        let botHtml = '<div class="messageContainer"><p class="botMessage">Bot: ' + getBotResponse(userText) + '</p></div>';
        $('#chatbox').append(botHtml);
        $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);
    });
});

function getBotResponse(userInput) {
    let botResponse = "";
    $.ajax({
        url: '/chat',
        data: JSON.stringify({ 
            'user_input': userInput,
            'previous_answers': previous_answers,
            'current_state': current_state
        }),
        contentType: 'application/json',
        type: 'POST',
        async: false, // Make the AJAX call synchronous
        success: function(response) {
            current_state = response['next_state'];
            previous_answers = response['previous_answers'];
            botResponse = response['question'];
        },
        error: function(error) {
            console.log(error);
        }
    });

    return botResponse;
}