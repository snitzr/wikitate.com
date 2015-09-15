$(document).ready(function() {
  // TODO: start function on playerReady
  setInterval(updateCurrentTime, 100);
  captionTime(0.0);

  // check for short youtube URL and redirect to short Wikitate URL
  if (/youtu.be\/(...........)/.test(location.href)) {
    var vidIdMatch = location.href.match(/youtu.be\/(...........)/, '$1')
    window.location = ('/' + vidIdMatch[1] +'/');
  }
  // TODO: match to share link language
  // if (/wikitate.com\/(...........)\//.test(location.href)) {
  //   var vidIdMatch = location.href.match(/youtu.be\/(...........)/, '$1')
  //   window.location = ('/' + vidIdMatch[1] +'/');
  // }
});

var transcript = {};

// video name headline change with onStateChange
function onStateChange(event) {
  if (player.getVideoData().title) {
    $('.vidNameNav').html(player.getVideoData().title); // replace vid headline ID with vid title
    $('title').append((' &#47; ') + (player.getVideoData().title)); // append video title to page title
  }
}

// video name to title on onPlayerReady
function onPlayerReady(event) {
  if (player.getVideoData().title) {
    $('.vidNameNav').html(player.getVideoData().title); // replace vid headline ID with vid title
    $('title').append((' &#47; ') + (player.getVideoData().title)); // append video title to page title
  }
}


// link timer to timestamp and display caption function
function updateCurrentTime() {
  if (player.getPlayerState() === 1) {
    var rounded = ((Math.round((player.getCurrentTime()) * 2)) / 2);
    $('.timestamp_display').html('<a href="#notlink">' + '&nbsp;&nbsp;&nbsp;&nbsp;' + Math.round(rounded) + '&nbsp;&nbsp;&nbsp;&rArr;</a>');
    captionTime(rounded);
  }
}



// append or delete new time and text row to add transcript table on click. TODO: reduce duplication.
$('#transcripting').on('click', 'td', function(event) {
  event.preventDefault(); // prevent placeholder link from appering in browser URL
    if ($(this).html() === '+') {
      var this_closest_tr = $(this).closest('tr');
      var transcripting_row = $(this_closest_tr).html();
      $(this_closest_tr).after('<tr>' + transcripting_row + '</tr>');
      $(this_closest_tr).next().children('.transcript_cell').children('input').focus();
  }
  else if ((($('#transcripting tr').length) > 2) && ($(this).html() === '-')) {
    $(this).closest('tr').remove();
  }
});

$('#transcripting').on('keyup', 'td', function(event) {
  event.preventDefault(); // prevent placeholder link from appering in browser URL
  if (event.keyCode === 13) {
    if ($(this).html() === '+') {
      var this_closest_tr = $(this).closest('tr');
      var transcripting_row = $(this_closest_tr).html();
      $(this_closest_tr).after('<tr>' + transcripting_row + '</tr>');
      $(this_closest_tr).next().children('.transcript_cell').children('input').focus();
    }
  }
  else if ((($('#transcripting tr').length) > 2) && ($(this).html() === '-')) {
    $(this).closest('tr').remove();
  }
});

// display captions to page and clear after six seconds
var captionTime;
captionTime = function(currentTime) {
  var endAndStartTimer;
  if (transcript[currentTime] !== undefined) {
    endAndStartTimer = function() {
      var displayFade;
      displayFade = function() {
        $("#captions").fadeOut('fast');
      };
      clearTimeout(window.hider);
      $('#captions').html(transcript[currentTime]).show();
      $('#captions').css({'z-index': '9999999'});
      console.log(transcript[currentTime]);
      window.hider = window.setTimeout(function() {
        displayFade();
      }, 6000);
    };
    window.hider;
    endAndStartTimer();
  }
};

// current time display --> timestamp field and trigger create JSON from transcript table
$('#transcripting').on('click mouseup', 'a', function(event) {
  event.preventDefault();
  if ((Math.round(((player.getCurrentTime()) * 2)) / 2) > 2.5) {
    var adjustTime = ((Math.round((player.getCurrentTime() * 2)) / 2) - 1);
    $(this).parent().next('td').children('input').val(adjustTime);
  } else {
    $(this).parent().next('td').children('input').val(Math.round(((player.getCurrentTime()) * 2)) / 2);
  }
  transcript2JSON();
})

// create JSON from transcript table
// TODO: clear any double blank text field rows after submit
$('#transcripting').on('keyup click', 'input', function() {
  transcript2JSON();
});
function transcript2JSON() {
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
  console.log(parsed_with_slice);
}



// form validation: prevent submit on enter from form field
$('#transcripting').on('keyup keypress', 'input', function(event) {
  var keycode = event.keyCode || event.which;
  if (keycode === 13) {
    event.preventDefault();
    return false;
  }
});

// form validation: prevent submit without drop down language choice
$('#submit').on('submit click keyup keypress', function(event) {
  if ($('#id_language').eq(0).val() === null) {
    event.preventDefault();
    var transcript_required_error_message = 'Transcript language required.';
    $('#language_message').html('&laquo; ' + transcript_required_error_message);
    $('#language_submit_message').html(transcript_required_error_message);
    return false;
  }
});

// form validation: prevent submit without all timestamps
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

// form validation: remove error message on langauge select after drop down choose
$('#id_language').on('change', function() {
  if ($(this).eq(0).val() === null) {
    return false;
  }
  else {
    $('#language_message').html('');
    $('#language_submit_message').html('');
  }
});

// form validation: remove error message on time select after time add
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



// kludge to replace language abbreviations with their full names
$('.language_abbr').each(function(index) {
  var shortLanguage = $(this).text();
  var mapObj = {
    'af': 'Afrikaans',
    'id': 'Bahasa Indonesia',
    'ms': 'Bahasa Malaysia',
    'ca': 'Català',
    'cs': 'Čeština',
    'da': 'Dansk',
    'de': 'Deutsch',
    'et': 'Eesti',
    'en_GB': 'English (UK)',
    'en': 'English (US)',
    'es': 'Español (España)',
    'es_419': 'Español (Latinoamérica)',
    'eu': 'Euskara',
    'fil': 'Filipino',
    'fr': 'Français',
    'fr_CA': 'Français (Canada)',
    'gl': 'Galego',
    'hr': 'Hrvatski',
    'zu': 'IsiZulu',
    'is': 'Íslenska',
    'it': 'Italiano',
    'sw': 'Kiswahili',
    'lv': 'Latviešu valoda',
    'lt': 'Lietuvių',
    'hu': 'Magyar',
    'nl': 'Nederlands',
    'no': 'Norsk',
    'pl': 'Polski',
    'pt_PT': 'Português',
    'pt': 'Português (Brasil)',
    'ro': 'Română',
    'sk': 'Slovenčina',
    'sl': 'Slovenščina',
    'fi': 'Suomi',
    'sv': 'Svenska',
    'vi': 'Tiếng Việt',
    'tr': 'Türkçe',
    'bg': 'Български',
    'ru': 'Русский',
    'sr': 'Српски',
    'uk': 'Українська',
    'el': 'Ελληνικά',
    'iw': 'עברית',
    'ur': 'اردو',
    'ar': 'العربية',
    'fa': 'فارسی',
    'mr': 'मराठी',
    'hi': 'हिन्दी',
    'bn': 'বাংলা',
    'gu': 'ગુજરાતી',
    'ta': 'தமிழ்',
    'te': 'తెలుగు',
    'kn': 'ಕನ್ನಡ',
    'ml': 'മലയാളം ',
    'th': 'ภาษาไทย',
    'am': 'አማርኛ',
    'zh_CN': '中文 (简体)',
    'zh_TW': '中文 (繁體)',
    'zh_HK': '中文 (香港)',
    'ja': '日本語',
    'ko': '한국어',
    'ot': 'other'
  }
  var newString = shortLanguage.replace(/\baf\b|\bid\b|\bms\b|\bca\b|\bcs\b|\bda\b|\bde\b|\bet\b|\ben_GB\b|\ben\b|\bes_419\b|\bes\b|\beu\b|\bfil\b|\bfr_CA\b|\bfr\b|\bgl\b|\bhr\b|\bzu\b|\bis\b|\bit\b|\bsw\b|\blv\b|\blt\b|\bhu\b|\bnl\b|\bno\b|\bpl\b|\bpt_PT\b|\bpt\b|\bro\b|\bsk\b|\bsl\b|\bfi\b|\bsv\b|\bvi\b|\btr\b|\bbg\b|\bru\b|\bsr\b|\buk\b|\bel\b|\biw\b|\bur\b|\bar\b|\bfa\b|\bmr\b|\bhi\b|\bbn\b|\bgu\b|\bta\b|\bte\b|\bkn\b|\bml\b|\bth\b|\bam\b|\bzh_CN\b|\bzh_TW\b|\bzh_HK\b|\bja\b|\bko\b|\bot\b/, function(matched){
    return mapObj[matched];
  });
  $(this).text(newString);
});

// enter edit transcript two column mode after dropdown selection
$('.show_hide_add_transcripts').on('change', function(event) {
  open_editor(event);
});
$('.transcript_choose_edit').on('mouseup', function(event) {
  open_editor(event);
});
function open_editor(event) {
  event.preventDefault(); // prevent placeholder link from appering in browser URL
  if ($('#add_transcripts').css('display') === 'none') {
    $('#add_transcripts').slideToggle(100);
    $('#transcription_tips').slideToggle(100);
    $('#transcript_table_scrollbox').slideToggle(100);
    $('#ytplayer').css({'height': '600px', 'width': '100%', 'display': 'inline-block', 'width': '40%'});
    $('#submitted_transcripts').css({'visibility': 'hidden', 'display': 'none'});
    $('#add_transcripts').css({'display': 'inline-block', 'float': 'left'});
    $('#submit_edit').css({'visibility': 'visible', 'display': 'block'});
    $('.transcript_input').focus();
  }
}

// hide edit transcript mode
$('#cancel_edit').on('click', function(event) {
  event.preventDefault();
  if (confirm('Cancel edit?')) {
    location.reload();
    // $('#add_transcripts').slideToggle(100);
    // $('#transcript_table_scrollbox').slideToggle(100);
    // $('#transcription_tips').slideToggle(100);
    // $('#ytplayer').css({'display': 'block', 'height': '200px', 'width': '25%'});
    // $('#submit_edit').css({'visibility': 'hidden', 'display': 'none'});
    // $('#submitted_transcripts').css({'visibility': 'visible', 'display': 'block'});
  } else {
    return
  }
});

// load existing transcript.
$('#id_language').on('change', function() {
  // var edit_content = ''
  var transcript_html_front_back = '<tr><td class="timestamp_display" title="Add timestamp to this row."><a href="#notlink">&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&rArr;</a></td> <td class="time_cell"><input class="timestamp_input mousetrap" name="timestamp_cell" cols="100" min="0" type="number" step="0.5" value="" /></td><td class="transcript_cell"><input class="transcript_input mousetrap" name="transcript_cell" maxlength="100" type="text" autocomplete="off" /></td> <td class="insert_row" tabindex="0">+</td> <td class="delete_row">-</td></tr>';
  var transcript_html_front_back_list = '';

  var json_lang = $('#json_lang_' + $('#id_language option:selected').attr('value')).html();
  var json_lang_parse = JSON.parse(json_lang);

  if (json_lang) {
    var json_parse = JSON.parse(json_lang);
    var foo_count = 0;
    for (var i = 0; i <= 20000; i += 0.5) {
      if (json_parse[i] !== undefined) {
        transcript_html_front_back_list += (transcript_html_front_back);
      }
    }
    $('.transcripting_info').replaceWith(transcript_html_front_back_list);

    // populate timestamp field(s)
    var key_counter = 0;
    $.each(json_lang_parse, function(key, value) {
      $('.timestamp_input').eq(key_counter).val(key);
      key_counter += 1;
    });
    // populate transcript field(s)
    var value_counter = 0;
    $.each(json_lang_parse, function(key, value) {
      $('.transcript_input').eq(value_counter).val(value);
      value_counter += 1;
    });

    transcript2JSON();
    
  } else {
    $('.transcripting_info').html(transcript_html_front_back);
  }
});

// transcript table JSON to display human readable format
$('.transcript_preview_cell').each(function(index) {
  var a_drop_concat = '';
  a_drop_down_value = JSON.parse($(this).text());
  // TODO: how to get all text if i <= x limits a large transcript?
  for (var i = 0; i <= 20000; i += 0.5 ) {
    if (a_drop_down_value[i] !== undefined) {
      a_drop_concat += (a_drop_down_value[i] + '<br>');
      $(this).html(a_drop_concat);
    }
  }
});

// load table selection after transcript selection
$('.transcript_choose_column_status').on('click', function() {
  $('#captions').html(''); // clear out current transcript display
  transcript = (JSON.parse($(this).siblings('.transcript_json_cell').text()));
  ($('.transcript_loaded_cell').text('► Play'));
  ($(this).html('.transcript_loaded_cell').text('Selected'));
  ($('.transcript_preview_row').css('backgroundColor', 'white'));
  ($(this).parent().css('backgroundColor', '#D8D8D8'));
  $('#ytplayer').animate({
    height: '600px',
    width: '100%'}
    , 150);
  // TODO: add logic to pause video if clicked when video is playing
  player.playVideo();
  $('html, body').scrollTop(50);
}); 

// top level page move search box to URL
$('#submit_vid_search').on('submit click', function(event) {
  event.preventDefault();
  // submit form content to URL
  window.location = ('//' + window.location.host + '/' + $('#id_transcript_search').val());
});

// START Mousetrap
// play pause video
Mousetrap.bind(['ctrl+space'], function() {
  if (player.getPlayerState() !== 1) {
    player.playVideo();
  } else {
    player.pauseVideo();
  }
  return false;
});

// write timestamp if focused and move to next timestamp field
Mousetrap.bind(['ctrl+t'], function() {
  if ($('.timestamp_input').is(':focus')) {
    if (((player.getCurrentTime() * 2) / 2) > 2.5) {
      $('.timestamp_input:focus').val((Math.round((player.getCurrentTime()) * 2) / 2) - 1);
    } else {
      $('.timestamp_input:focus').val((Math.round((player.getCurrentTime()) * 2) / 2));
    }
  }
    // move focus to next
    $('.timestamp_input:focus').parent().parent().next().find('.timestamp_input').focus();
    return false;
  });

// skip back one second
Mousetrap.bind(['ctrl+r'], function() {
  // player.pauseVideo();
  player.seekTo((player.getCurrentTime() - 1), true);
  console.log('back one second');
  // player.playVideo();
});

// END Mousetrap


// TODO: test for videos that cannot be embeded
// function onError(event) {
//   throw event
// }


// TESTING: jump timer vid to field time
// $('.transcript_input').on('focus', function() {
  // TODO: seekTo auto starts the video. needs to auto start / not auto start based on context. Example: not autostart if timestamp empty.
  // TODO: make auto start work for dynamicly generated rows.
  // if (player.seekTo(($(this).closest('tr').find('input.timestamp_input').val()))) {
    // alert('yo');
  // }
// });


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
// $('#starp').click(function() {
//   if (player.getPlayerState() === 1) {
//     player.pauseVideo();
//   } else {
//     player.playVideo();
//   }
// });

// // skip back control
// $('#skipBack').click(function() {
//   player.pauseVideo();
//   player.seekTo((player.getCurrentTime() - 3), true);
//   player.playVideo();
//   // console.log(player.getCurrentTime());
// });

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

// begin vid title replacement (DEPRICATED)
// var intervalHead, intervalHeadStop;
// function changeTitle() {
  // intervalHead = setInterval(titleReplace, 100);
  // intervalHeadStop = setTimeout(titleReplaceStop, 5000); // prevent infinite title search
// }
// function titleReplace() {
  // if (player.getVideoData().title) {
    // $('.vidNameNav').html(player.getVideoData().title); // replace vid headline ID with vid title
    // $('title').append((' &#47; ') + (player.getVideoData().title)); // append video title to page title
    // clearInterval(intervalHead);
  // }
// }
// function titleReplaceStop() {
    // clearInterval(intervalHead);
// }
// end vid title replacement




// show hide add transcript and tips and resize player
// $('#show_hide_add_transcripts').on('click', function(event) {
//   event.preventDefault(); // prevent placeholder link from appering in browser URL
//   if ($('#add_transcripts').css('display') === 'none') {
//     $('#add_transcripts').slideToggle(100);
//     $('#transcription_tips').slideToggle(100);
//     $('#transcript_table_scrollbox').slideToggle(100);
//     $('#add_transcripts').css({'display': 'inline-block'});
//     $('#ytplayer').css({'display': 'inline-block', 'width': '50%'});
//   } else {
//     $('#add_transcripts').slideToggle(100);
//     $('#transcript_table_scrollbox').slideToggle(100);
//     $('#transcription_tips').slideToggle(100);
//     $('#ytplayer').css({'display': 'block', 'width': '100%'});
//   }
// });
