$(document).ready(function() {
  setInterval(updateCurrentTime, 100);
  captionTime(0.0);
  changeTitle(); // start search for video title to insert into headline
});

// begin vid title replacement
var intervalHead, intervalHeadStop;
function changeTitle() {
  intervalHead = setInterval(titleReplace, 100);
  intervalHeadStop = setTimeout(titleReplaceStop, 5000); // prevent infinite title search
}
function titleReplace() {
  if (player.A.videoData.title) {
    $('.vidNameNav').html(player.A.videoData.title); // replace vid headline ID with vid title
    clearInterval(intervalHead);
  }
}
function titleReplaceStop() {
    clearInterval(intervalHead);
}
// end vid title replacement

$('#timeStamp').html('&nbsp;');


// link timer to timestamp and display caption function
// TODO: time on user side, check API time as failsafe near user next caption time.
function updateCurrentTime() {
  if (player.getPlayerState() === 1) {
    // v2 why round? why not just match nonround to last transcript event?
    var rounded = (Math.round(((player.getCurrentTime()) * 2)) / 2);
    $('#timeStamp').html('Timestamp: ' + 'rounded: ' + rounded + ' fixed: ' + player.getCurrentTime().toFixed(1));
    captionTime(rounded);
  }
}

var transcript = {};

// display captions to page and clear after six seconds
var captionTime;
captionTime = function(currentTime) {
  var endAndStartTimer;
  if (transcript[currentTime] !== undefined) {
    endAndStartTimer = function() {
      var displayFade;
      displayFade = function() {
        $("#captions").fadeOut("fast");
      };
      clearTimeout(window.hider);
      $("#captions").html(transcript[currentTime]).show();
      window.hider = window.setTimeout(function() {
        displayFade();
      }, 6000);
    };
    window.hider;
    endAndStartTimer();
  }
};




// jump timer vid to field time TESTING
/*
$('#timing').on('click', function() {
  player.seekTo((document.getElementById('timing').innerHTML), true); //seekTo argument needs evaluation
});
*/

// load captions on click
// $('.transcriptDisplaySelect').click(function() {
//   if (player.getPlayerState() === 1) {
//     player.playVideo();
//   }
//   $('#captions').html(''); // clear current transcript display
//   transcript = $.parseJSON($(this).html());
//   // autostart vid
//   alert(player);
// });

// start / stop video control
$('#starp').click(function() {
  if (player.getPlayerState() === 1) {
    player.pauseVideo();
  } else {
    player.playVideo();
  }
});

// skip back control
$('#skipBack').click(function() {
  player.pauseVideo();
  player.seekTo((player.getCurrentTime() - 3), true);
  player.playVideo();
  // console.log(player.getCurrentTime());
});

// load transcript cells on language selection
/* 
$('#submit').on('submit click keyup keypress', function(event) {
  if ($('#id_language').eq(0).val() === null) {
    event.preventDefault();
    var transcript_required_error_message = 'Transcript language required.';
    $('#language_message').html('&laquo; ' + transcript_required_error_message);
    $('#language_submit_message').html(transcript_required_error_message);
    return false;
  }
});
*/

// append new time and text row to add transcript table on click
$('#transcripting').on('click', 'a', function(event) {
  event.preventDefault(); // prevent placeholder link from appering in browser URL
  // console.log($(this).html());
  if ($(this).html() === '+') {
    var this_closest_tr = $(this).closest('tr');
    var transcripting_row = $(this_closest_tr).html();
    $(this_closest_tr).after('<tr>' + transcripting_row + '</tr>');
    $(this_closest_tr).next().children('.transcript_cell').children('input').focus();
  }
  else if (($('#transcripting tr').length) > 2) {
    $(this).closest('tr').remove();
  }
});

// create JSON from transcript table
// TODO: clear any double blank text field rows after submit
// TODO: maybe add JSON parse to only work on already submitted text and not while submitting. do submit in Python
$('#transcripting').on('keyup click', 'input', function() {
  var transcripting_form_values = JSON.stringify($('#transcripting :input, textarea').serializeArray());
  var parsed_add = '{';
  var parsed = JSON.parse(transcripting_form_values);
  for (var i = 0; i < transcripting_form_values.length; i++) {
    if (typeof parsed[i] !== 'undefined') {
      if ((parsed[i].name) === ('timestamp_cell')) {
        parsed_add += ('"' + parsed[i].value + '": ');
      }
      else if ((parsed[i].name) === ('transcript_cell')) {
        // replace danger characters with safe equivalent
        var parsed_escaped = parsed[i].value.replace(/\&/gi, '&amps;');
        parsed_escaped = parsed_escaped.replace(/\"/gi, '&quot;');
        parsed_escaped = parsed_escaped.replace(/\\/gi, '&#92;');
        parsed_add += ('\"' + parsed_escaped + '\"' + ', ');
      }
    }
    var parsed_with_slice = (parsed_add.slice(0, -2) + '}');
  }
  $('#id_transcript').val(parsed_with_slice);
  transcript = JSON.parse(parsed_with_slice); // live preview in YT vid
});

// prevent submit on enter from form field
$('#transcripting').on('keyup keypress', 'input', function(event) {
  var keycode = event.keyCode || event.which;
  if (keycode === 13) {
    event.preventDefault();
    return false;
  }
});

// prevent submit without drop down language choice
$('#submit').on('submit click keyup keypress', function(event) {
  if ($('#id_language').eq(0).val() === null) {
    event.preventDefault();
    var transcript_required_error_message = 'Transcript language required.';
    $('#language_message').html('&laquo; ' + transcript_required_error_message);
    $('#language_submit_message').html(transcript_required_error_message);
    return false;
  }
});

// prevent submit without all timestamps
$('#submit').on('submit click keyup keypress', function(event) {
  for (var i = 0; i <= $('#transcripting .time_cell').children().length; i++) {
    if ($('.timestamp_input').eq(i).val() === '') {
      event.preventDefault();
      $('.timestamp_input').eq(i).css('border', '2px solid red');
      var transcript_required_error_message = 'Time value(s) required.';
      $('#time_submit_message').html(transcript_required_error_message);
    }
  }
});

// remove error message on langauge select after drop down choose
$('#id_language').on('change', function() {
  if ($(this).eq(0).val() === null) {
    return false;
  }
  else {
    $('#language_message').html('');
    $('#language_submit_message').html('');
  }
});

// remove error message on time select after time add
$('#transcripting').on('keyup click', 'input', function() {
  $('.timestamp_input').each(function() {
    if ($(this).val() === '') {
      return;
    }
    if ($(this).val() !== '') {
      $(this).css('border', '1px solid #454545');
      return;
    }
  });
  for (var i = 0; (i <= $('#transcripting .time_cell').children().length); i++) {
    console.log($('.timestamp_input').eq(i).val());
    if ($('.timestamp_input').eq(i).val() === '') {
      break;
    }
    else {
      if (i === $('#transcripting .time_cell').children().length) {
        $('#time_submit_message').html('');
      }
    }
  }
});

// // drop down JSON to human readable format
// $('#transcript option').each(function(index) {
//   var drop_concat = '';
//   if (index !== 0) {
//     drop_down_value = JSON.parse(this.value);
//     for (var i = 0; i <= 20; i += 0.5 ) {
//       if (drop_down_value[i] !== undefined) {
//         drop_concat += (drop_down_value[i] + ' ');
//         $(this).html(drop_concat);
//       }
//     }
//   }
// });

// load drop down selection after choice select and show load message
// $('#transcript').on('change', runction() {
//   $('#captions').html(''); // clear current transcript display
//   transcript = (JSON.parse(this.value));
// });

// // TESTING: load drop down selection after choice select and show load message
// $('.transcript_preview_cell').on('click', function() {
//   $('#captions').html(''); // clear current transcript display
//   transcript = (JSON.parse(this.value));
// });

// Transcript table JSON to display human readable format
$('.transcript_preview_cell').each(function(index) {
  var a_drop_concat = '';
  a_drop_down_value = JSON.parse($(this).text());
  // TODO: how to get all text if i <= x limits a large transcript?
  for (var i = 0; i <= 20000; i += 0.5 ) {
    if (a_drop_down_value[i] !== undefined) {
      a_drop_concat += (a_drop_down_value[i] + '<br />');
      $(this).html(a_drop_concat);
    }
  }
});



// Load table selection after choice select
$('.transcript_preview_row').on('click', function() {
  $('#captions').html(''); // clear out current transcript display
  transcript = (JSON.parse($(this).children('.transcript_json_cell').text()));
  ($('.transcript_loaded_cell').text(''));
  ($(this).children('.transcript_loaded_cell').text('Selected'));
  ($('.transcript_preview_row').css('backgroundColor', 'white'));
  ($(this).css('backgroundColor', '#D8D8D8'));
  player.playVideo();
}); 

// top level page move search box to URL
$('#submit_vid_search').on('submit click', function(event) {
  event.preventDefault();
  // submit form content to URL
  window.location = ('//' + window.location.host + '/' + $('#id_transcript_search').val());
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

// find vidID for meta JSON info
// var vidCode = $('#vidCode').html(vidCode);
// var vidCode = /v=11+/g.exec(vidCode); // or val.replace (,);
// $('#returnYT').html('\"<a href=\"//youtube.com/watch?v=\"' + vidCode + 'returnYT</a>');

// return to YouTube button
// $('#returnYT').html('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// $('#returnYT').html(player.getVideoUrl());

/*
$('#returnYT').click(function() {
  console.log(player.getVideoUrl());
});
*/

// $('#returnYT').click(function() {
  // return document.URL = ('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// });

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);


// not getting latest form edit content
// test
// $('#text').keyup(function() {
//   var activeForm = (document.getElementById('text').innerHTML);
//   console.log(activeForm);
// });

// return to YouTube button
// $('#returnYT').html('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// $('#returnYT').html(player.getVideoUrl());
// $('#returnYT').click(function() {
  // return document.URL = ('//www.youtube.com/watch?v=' + {{ vidId|escapejs }});
// });

// best alternative to yt.setConfig search is search page for FEEDBACK_LOCALE_LANGUAGE
//var userLanguage = $('script').text().match(/'FEEDBACK_LOCALE_LANGUAGE': ".*?"/).toString().match(/".*?"/).toString().replace(/\"/g, '');
//$('#' + userLanguage).attr('selected', true);



















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

// display captions to page and clear after six seconds. Legacy.
// function captionTime(currentTime) {
//   if ((transcript[currentTime]) !== undefined) {
//     window.hider;
//     endAndStartTimer();
//     function endAndStartTimer() {
//       clearTimeout(window.hider);
//       $('#captions').html(transcript[currentTime]).show(); // display transcript
//       window.hider = window.setTimeout(function() {
//           displayFade()
//         }, 6000);
//       function displayFade() {
//         $('#captions').fadeOut('fast')
//       };
//     }
//   }
// }

// live reload
document.write('<script src="http://' + (location.host || 'localhost').split(':')[0] + ':35729/livereload.js?snipver=1"></' + 'script>')