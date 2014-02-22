// load video timer display
function onYouTubePlayerReady(playerId) {
  window.ytvid = document.getElementById('myytplayer');
  console.log('Player state ' + (ytvid.getPlayerState().toString()));
  setInterval(updateCurrentTime, 100);
  captionTime(0.0);
}
// the updateCurrentTime function could be made more generic maybe with video name as an argument
function updateCurrentTime() {
  if (ytvid.getPlayerState() === 1) {
    $('#timeStamp').html(ytvid.getCurrentTime().toFixed(1));
    captionTime(ytvid.getCurrentTime());
  }
}
var transcript = {0: 'This a test of the CamStudio microphone.', 3: 'It\'s just dangling from my ear.', 5: 'Um, this is how we learn math.', 10: 'Whoops!', 13.0: 'Let\'s click click click delete "h."', 18.5: 'Good.', 20: '', 24.0: 'Is it not recording?', 25.8: ''};
function captionTime(currentTime) {
  if ((transcript[Math.round(currentTime * 10) / 10]) === undefined) {          
    // console.log((Math.round(currentTime * 10) / 10) + '\tu');
  }
  else {
    $('#captions').html(transcript[Math.round(currentTime * 10) / 10]);
    // console.log((Math.round(currentTime * 10) / 10) + '\tsub');
  }
}

// start / stop video control
$('#starp').click(function() {
  if (ytvid.getPlayerState() === 1) {
    ytvid.pauseVideo(); 
  }
  else {
    ytvid.playVideo();
  }
});

// skip back control
$('#skipBack').click(function() {
  ytvid.seekTo((ytvid.getCurrentTime() - 1), true);
  console.log(ytvid.getCurrentTime());
});

// mark time with mouse click
$('#timeClick').mousedown(function() {
  console.log(ytvid.getCurrentTime());
});
$('#timeClick').mouseup(function() {
  console.log(ytvid.getCurrentTime());
});

// find YT username
// $('#username').html(document.getElementById('yt-masthead-user-displayname').innerHTML);

// find vidID
$('#vidCode').html(vidCode);

// return to YouTube button
$('a#returnYT').click(function() {
  return document.URL = ('//www.youtube.com/' + vidURL);
});

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);


// not getting latest form edit content
$('#text').keyup(function() {
  var activeForm = (document.getElementById('text').innerHTML);
  console.log(activeForm);
});
