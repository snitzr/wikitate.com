$(window).load(function () {
  setInterval(updateCurrentTime, 100);
  captionTime(0.0);
});

// link timer to timestamp and display caption function
// v2 time on user side, check API time as failsafe near user next caption time.
function updateCurrentTime() {
  $('#timeStamp').html('&nbsp;');
  if (player.getPlayerState() === 1) {
    // v2 why round? why not just match nonround to last transcript event?
    var rounded = (Math.round(((player.getCurrentTime()) * 2)) / 2);
    $('#timeStamp').html('Timestamp: ' + 'rounded: ' + rounded + ' fixed: ' + player.getCurrentTime().toFixed(1));
    console.log(player.getCurrentTime());
    console.log(rounded + ' rounded');
    captionTime(rounded);
  }
}


var transcript = {
  "0": "0",
  0.5: "hello",
}

// v2 caption format?
// [{"time":"3", "time":3, "text":"hello"}, ...]

//var transcript = {
  //"0": "This a test of the CamStudio microphone.",
  //"3": "It\'s just dangling from my ear.",
  //"5": "Um, this is how we learn math.",
  //"10": "Whoops!",
  //"13": "Let\'s click click click delete \"h.\"",
  //"17.5": "Good.",
  //"20": "",
  //"24": "Is it not recording?",
  //"25": ""
//};


// jump timer vid to field time TESTING
/*
$('#timing').click(function () {
  player.seekTo((document.getElementById('timing').innerHTML), true); //seekTo argument needs evaluation
});
*/

// display captions to page
function captionTime(currentTime) {
  if ((transcript[currentTime]) !== undefined) {
    $('#captions').html(transcript[currentTime]);
  }
}

// select captions on click
$('.transcriptDisplaySelect').click(function () {
  // add click content to transcript var
  $('#captions').html(''); // clear current transcript display
  transcript = $(this).text();
  transcript = $.parseJSON(transcript);
});

// start / stop video control
$('#starp').click(function () {
  if (player.getPlayerState() === 1) {
    player.pauseVideo(); 
  } else {
    player.playVideo();
  }
});

// skip back control
$('#skipBack').click(function () {
  player.seekTo((player.getCurrentTime() - 1), true);
  console.log(player.getCurrentTime());
});

// mark time with mouse click
$('#timeClick').mousedown(function () {
  console.log(player.getCurrentTime());
});
$('#timeClick').mouseup(function () {
  console.log(player.getCurrentTime());
});



// append new time and text line to add transcript table on tab
// clear any double blank rows after submit
// allow tab through to Submit button if last text field is blank
// make this function a variable to call? Currently having global vs local var issue because declaring var in function?
$('#transcripting').on('click', 'a', function() {
  var this_closest_tr = $(this).closest('tr'); // declare this tr as fast reusable var
  var transcripting_row = ($(this_closest_tr).html());
  $(this_closest_tr).after('<tr>' + transcripting_row + '</tr>');
  $(this_closest_tr).next().children('.transcript_cell').children('input').focus();
  return false;
  });

$('#transcripting').on('keyup', 'input', function() {
  // var transcripting_form_values = $(this).val();
  var transcripting_form_values = $('#transcripting').filter(':input').val();
  console.log(transcripting_form_values);
  // console.log($('#transcripting:input').val());
  $('#concat_transcript').val(transcripting_form_values);
});

/*
$('#transcripting').on('focusin', function() {
  // need logic to only append on last row
  // need logic to stop appending once new blank row is appended
  // jQuery logic to see if next tag is not table so to only append last row
  // tab order needs to be respected
  // add overflow feature in CSS
  console.log('\nworking_________________v\n');
  console.log('1a activeElement val:\t' + $(document.activeElement).val());
  console.log('1b activeElement type:\t' + document.activeElement.type);
*/

  /*
  if ((document.activeElement) === $('#transcripting tr:last')) {
    console.log('last in focus');
  }
  */

  // $('#transcripting tr:last').css('background-color', 'red');
  // $('#transcripting tr:last').prev().css('background-color', 'white');

  // if last row, if text, if !(prev prev row text False and prev row text False).
  // if ((document.activeElement.type === 'text') /*&& (document.activeElement.value === '') && ('test' === 'test')*/) {
    // for maintainability the appended HTML should just make a copy of current tr minus text input and not be hardcoded HTML
    // $('#transcripting').append('<tr><td class="time_cell"><input cols="100" min="0" type="number" placeholder="time" autocomplete="off" step="0.5"</td><td class="transcript_cell"><input maxlength="100" type="text" placeholder="text" autocomplete="off"></td><td>+</td></tr>');
   // }
// });



















// find YT username
// $('#username').html(document.getElementById('yt-masthead-user-displayname').innerHTML);

// find vidID
$('#vidCode').html(vidCode);
// $('#returnYT').html('\"<a href=\"//youtube.com/watch?v=\"' + vidCode + 'returnYT</a>');

// return to YouTube button
// $('#returnYT').html('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// $('#returnYT').html(player.getVideoUrl());

$('#returnYT').click(function () {
  console.log(player.getVideoUrl());
});
// $('#returnYT').click(function () {
  // return document.URL = ('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// });

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);


// not getting latest form edit content
$('#text').keyup(function () {
  var activeForm = (document.getElementById('text').innerHTML);
  console.log(activeForm);
});

// return to YouTube button
// $('#returnYT').html('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// $('#returnYT').html(player.getVideoUrl());
$('#returnYT').click(function () {
  console.log(player.getVideoUrl());
});
// $('#returnYT').click(function () {
  // return document.URL = ('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// });

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);


// not getting latest form edit content
$('#text').keyup(function () {
  var activeForm = (document.getElementById('text').innerHTML);
  console.log(activeForm);
});

















// sandboxing
//
/*
$(window).load(intervalTimer(faster, 0, 100, 10000));

function intervalTimer(f, start, interval, end) {
  if (!start) start = 0;                // Default to 0 ms
  if (arguments.length <= 2) {          // Single-invocation case
    setTimeout(f, start);               // Single invocation after start ms.
  }
  else {                                // Multiple invocation case
    setTimeout(repeat, start);          // Repetitions begin in start ms
    function repeat() {                 // Invoked by the timeout above             
      var h = setInterval(f, interval); // Invoke f every interval ms. And stop invoking after end ms, if end is defined             
      if (end) setTimeout(function () { clearInterval(h); }, end);
    }
  }
}
*/

/*
$(window).load(faster);
function faster() {
  for (var i = 0; i < 200; i++) {
    if ((player()) === (-1)) {
      console.log('defined player');
    }
    else {
      if ((player()) !== undefined) {
        console.log('defined player');
      }
    }
  }
};
*/

// delay interval load
// $(window).load(window.setTimeout(funcX, 5500));


/*
remanants of cell traversal testing
console.log('2a this prev prev val:\t' + $(this).prev().prev().val());
console.log('2b this prev val:\t' + $(this).prev().val());
console.log('2c this prev:\t' + $(this).prev());
console.log('2d this siblings:\t' + $(this).siblings());
console.log('2e this next val:\t' + $(this).next().val()); // to check if next item is Submit button
console.log('2f this val:\t' + $(this).val()); // to check if next item is Submit button
console.log('3 this parent parent prev children val:\t' + $(this).parent().parent().prev().children().children().val());
console.log('4 #transcripting next val:\t' + $('#transcripting').next().val());
console.log('5 #transcripting last val:\t' + $('#transcripting').last().val());
console.log('6 last val:\t' + $('#transcripting').last().val());
console.log('7 #transcripting tr:last value:\t' + $('#transcripting tr:last').value);
console.log('8a #transcripting tr:last val:\t' + $('#transcripting tr:last').val());
console.log('8b #transcripting last val:\t' + $('#transcripting input').last().val());
console.log('8c #transcripting last prev val:\t' + $('#transcripting input').last().prev().val());
console.log('9a #transcripting type nth 2:\t' + $('#transcripting input:nth-last-of-type(2)').type);
console.log('9b #transcripting type nth 3:\t' + $('#transcripting input:nth-last-of-type(3)').type);
*/
