// load video interval
$(window).load(beginTimer);
function beginTimer() {
  setInterval(updateCurrentTime, 150);
  captionTime(0.0);
};

// link timer to timestamp and display caption function
function updateCurrentTime() {
  $('#timeStamp').html('&nbsp;');
  if (typeof(player) !== 'undefined') {
    if (player.getPlayerState() === 1) {
      var rounded = (Math.round(((player.getCurrentTime()) * 2)) / 2);
      $('#timeStamp').html('rounded: ' + rounded + ' fixed: ' + player.getCurrentTime().toFixed(1));
      console.log(player.getCurrentTime());
      console.log(rounded + ' rounded');
      captionTime(rounded);
    }
  }
}
var transcript = {0: 'This a test of the CamStudio microphone.', 3: 'It\'s just dangling from my ear.', 5: 'Um, this is how we learn math.', 10: 'Whoops!', 13.0: 'Let\'s click click click delete "h."', 17.5: 'Good.', 20: '', 24.0: 'Is it not recording?', 25.0: ''};

// add captions to page
function captionTime(currentTime) {
  if ((transcript[currentTime]) !== undefined) {
    $('#captions').html(transcript[currentTime]);
  }
}

// start / stop video control
$('#starp').click(function() {
  if (player.getPlayerState() === 1) {
    player.pauseVideo(); 
  }
  else {
    player.playVideo();
  }
});

// skip back control
$('#skipBack').click(function() {
  player.seekTo((player.getCurrentTime() - 1), true);
  console.log(player.getCurrentTime());
});

// mark time with mouse click
$('#timeClick').mousedown(function() {
  console.log(player.getCurrentTime());
});
$('#timeClick').mouseup(function() {
  console.log(player.getCurrentTime());
});

// find YT username
// $('#username').html(document.getElementById('yt-masthead-user-displayname').innerHTML);

// find vidID
$('#vidCode').html(vidCode);
// $('#returnYT').html('\"<a href=\"//youtube.com/watch?v=\"' + vidCode + 'returnYT</a>');

// return to YouTube button
// $('#returnYT').html('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// $('#returnYT').html(player.getVideoUrl());

$('#returnYT').click(function() {
  console.log(player.getVideoUrl());
});
// $('#returnYT').click(function() {
  // return document.URL = ('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// });

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);


// not getting latest form edit content
$('#text').keyup(function() {
  var activeForm = (document.getElementById('text').innerHTML);
  console.log(activeForm);
});

// return to YouTube button
// $('#returnYT').html('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// $('#returnYT').html(player.getVideoUrl());
$('#returnYT').click(function() {
  console.log(player.getVideoUrl());
});
// $('#returnYT').click(function() {
  // return document.URL = ('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// });

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);


// not getting latest form edit content
$('#text').keyup(function() {
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
      if (end) setTimeout(function() { clearInterval(h); }, end);
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
