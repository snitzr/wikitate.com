$(window).load(function () {
  setInterval(updateCurrentTime, 100);
  captionTime(0.0);
});

// link timer to timestamp and display caption function
function updateCurrentTime() {
  $('#timeStamp').html('&nbsp;');
  if (player.getPlayerState() === 1) {
    var rounded = (Math.round(((player.getCurrentTime()) * 2)) / 2);
    $('#timeStamp').html('Timestamp: ' + 'rounded: ' + rounded + ' fixed: ' + player.getCurrentTime().toFixed(1));
    console.log(player.getCurrentTime());
    console.log(rounded + ' rounded');
    captionTime(rounded);
  }
}


var transcript = {
  "0": "0",
}

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
// allow tab through to Submit button if last text field is blank
$(this).focusin(function() {
  // need logic to only append on last row
  // need logic to stop appending once new blank row is appended
  // jQuery logic to see if next tag is not table so to only append last row
  if ((((document.activeElement).type) === 'text') && ((document.activeElement).value) !== '') {
    // for maintainability the appended HTML should just make a copy of current tr minus text input and not be hardcoded HTML
    $('#transcripting').append('<tr id="runout_row"><td><input class="time" cols="100" min="0" type="number" placeholder="time" autocomplete="off" step="0.5"></td><td id="runout_line"><input class="transcript_cell" maxlength="100" placeholder="text" type="text" autocomplete="off"></td></tr>');
  }
  console.log('working');
  console.log((document.activeElement).value);
  console.log((document.activeElement).type);
  var runout =  $("#runout_line").next();
  // if runout === '' {
    // console.log('null next sibling');
  // }
});



















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
