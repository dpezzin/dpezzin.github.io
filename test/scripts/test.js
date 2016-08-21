$(document).ready(function() {
  $('#btnTest').click(function() {
    ShowCustomDialog();
  });
});


function ShowCustomDialog() {
  ShowDialogBox('Warning', 'We have two dental offices. Which would you like to call?', 'Call Mohegan Lake', 'Call Terrytown', 'GoToAssetList', null);
}

function ShowDialogBox(title, content, btn1text, btn2text, functionText, parameterList) {
  var btn1css;
  var btn2css;

  if (btn1text == '') {
    btn1css = "hidecss";
  } else {
    btn1css = "showcss";
  }

  if (btn2text == '') {
    btn2css = "hidecss";
  } else {
    btn2css = "showcss";
  }
  $("#lblMessage").html(content);

  $("#dialog").dialog({
    resizable: false,
    title: title,
    modal: true,
    width: '400px',
    height: 'auto',
    bgiframe: false,
    hide: {
      effect: 'scale',
      duration: 400
    },

    buttons: [{
      text: btn1text,
      "class": btn1css,
      click: function() {

        $("#dialog").dialog('close');

      }
    }, {
      text: btn2text,
      "class": btn2css,
      click: function() {
        $("#dialog").dialog('close');
      }
    }]
  });
}

function DlgShow(Message)
{
  // Change the message.
  var Msg = document.getElementById("DlgContent");
  Msg.innerHTML = Message;
 
  // Display the dialog box.
  var Dlg = document.getElementById("Overlay");
  Dlg.style.visibility = "visible";
}

function DlgHide(Result)
{
  // Display the result onscreen.
  var Output = document.getElementById("Result");
  Output.innerHTML = "You clicked: " + Result;
 
  // Hide the dialog box.
  var Dlg = document.getElementById("Overlay");
  Dlg.style.visibility = "hidden";
}