// load video timer display
function beginTimer() {
  // window.ytvid = document.getElementById('myytplayer');
  console.log('Player state ' + (player.getPlayerState().toString()));
  setInterval(updateCurrentTime, 150);
  captionTime(0.0);
};
// player update
// link timer to timestamp and display caption function
function updateCurrentTime() {
  if (player.getPlayerState() === 1) {
    $('#timeStamp').html(player.getCurrentTime().toFixed(1));
    console.log(player.getCurrentTime());
    captionTime(player.getCurrentTime());
  }
}
var transcript = {0: 'This a test of the CamStudio microphone.', 3: 'It\'s just dangling from my ear.', 5: 'Um, this is how we learn math.', 10: 'Whoops!', 13.0: 'Let\'s click click click delete "h."', 18.5: 'Good.', 20: '', 24.0: 'Is it not recording?', 25.0: ''};

// add captions to page
function captionTime(currentTime) {
  if ((transcript[Math.round(currentTime * 10) / 10]) === undefined) {            }
  else {
    $('#captions').html(transcript[Math.round(currentTime * 10) / 10]);
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

// player update
// skip back control
$('#skipBack').click(function() {
  player.seekTo((player.getCurrentTime() - 1), true);
  console.log(player.getCurrentTime());
});

// player update
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

// delay timer load
$(window).load(window.setTimeout(slower, 2500));
function slower() {
  beginTimer();
}
