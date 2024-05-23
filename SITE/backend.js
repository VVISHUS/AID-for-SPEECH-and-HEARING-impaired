CWASA.getLogger("Avatar", "info");

function playURL(surl) {
	CWASA.playSiGMLURL(surl);
}

function playText(stext) {
	CWASA.playSiGMLText(stext);
}

CWASA.addHook("status", addStatus);

function addStatus(evt) {
	var elt = document.getElementById("myStatusLog");
	var msg = evt.msg;
	if (evt.av != "*") {
		msg = "[av" + evt.av + "] " + msg;
	}
	elt.value = elt.value + msg + "\n";
}

CWASA.addHook("sigmlloading", startJSON);
CWASA.addHook("sigmlsign", writeJSON);
CWASA.addHook("sigmlloaded", endJSON);
var signSeq = 0;

function startJSON(evt) {
	var elt = document.getElementById("JSONText");
	if (elt) {
		elt.value = "[\n";
		signSeq = 0;
	}
}

function writeJSON(evt) {
	var elt = document.getElementById("JSONText");
	if (elt) {
		if (signSeq > 0) elt.value += ",\n"
		signSeq++;
		elt.value += JSON.stringify(evt.msg);
	}
}

function endJSON(evt) {
	var elt = document.getElementById("JSONText");
	if (elt) {
		elt.value += "\n]\n";
	}
}

CWASA.addHook("avatarfps", setFPS, 0);

function setFPS(evt) {
	var elt = document.getElementById("myFPS");
	elt.value = evt.msg.toFixed(2);
}

CWASA.addHook("avatarsign", setSignFrame, 0);

function setSignFrame(evt) {
	var msg = evt.msg;
	var elt = document.getElementById("mySF");
	elt.value = (msg.s+1)+"/"+(msg.f+1);
	elt = document.getElementById("myGloss");
	elt.value = msg.g;
}





////////////////////////////////////////////////////////////////
    
    
let isRecording = false;
let mediaRecorder;
let chunks = [];

const btnStart = document.getElementById('btnStart');
const btnStop = document.getElementById('btnStop');

btnStart.addEventListener('click', startRecording);
btnStop.addEventListener('click', stopRecording);

function startRecording() {
  if (!isRecording) {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = (event) => {
          chunks.push(event.data);
        };
        mediaRecorder.onstop = () => {
          const blob = new Blob(chunks, { type: 'audio/webm' });
          const url = URL.createObjectURL(blob);
          const downloadLink = document.createElement('a');
          downloadLink.href = url;
          downloadLink.download = 'recording.webm';
          downloadLink.click();
          chunks = [];
        };
        mediaRecorder.start();
        isRecording = true;
      })
      .catch(error => {
        console.error(error);
      });
  }
}

function stopRecording() {
  if (isRecording) {
    mediaRecorder.stop();
    isRecording = false;
	executePython();
  }
}

const loader = document.querySelector('.loader');

// Add event listener to start button
btnStart.addEventListener('click', function() {
    loader.classList.remove('hidden'); 
});

window.addEventListener('load', function () {
    loader.classList.add('hidden');
});


function executePython() {
        $.ajax({
            url: 'http://127.0.0.1:5000/execute_python',
            type: 'POST',
            success: function(response) {
                alert('SUCCESS!!...Sign Language Generated:', response);
            },
            error: function(error) {
                alert('Error executing script:', error);
            }
        });
    }

function execute_python_txt() {
        $.ajax({
            url: 'http://127.0.0.1:5000/execute_python_txt',
            type: 'POST',
            success: function(response) {
                alert('SUCCESS!!...Sign Language Generated:', response);
            },
            error: function(error) {
                alert('Error executing script:', error);
            }
        });
    }


// function upload_music() {
//     var musicFile = document.getElementById("musicFile").files[0];
//     var formData = new FormData();
//     formData.append('music', musicFile);

//     fetch('/upload_music', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         }
//         throw new Error('Network response was not ok.');
//     })
//     .then(data => {
//         console.log('Python function executed:', data);
//     })
//     .catch(error => {
//         console.error('Error executing Python function:', error);
//     });
// }

function saveTextAsFile() {

    var textToSave = document.getElementById("textInput").value;
    
    var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
    
    var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
    
    var fileNameToSaveAs = "input_text.txt";
    
    var downloadLink = document.createElement("a");
    
    downloadLink.download = fileNameToSaveAs;
    
    downloadLink.innerHTML = "Download File";
    
    downloadLink.href = textToSaveAsURL;
    
    downloadLink.onclick = destroyClickedElement;
    
    downloadLink.style.display = "none";
    
    document.body.appendChild(downloadLink);
    
    downloadLink.click();

    execute_python_txt()
    
    }
    
    function destroyClickedElement(event) {
    
    document.body.removeChild(event.target);
    
    }
    
    function clearCache() {
        fetch('/clear-cache', {
            method: 'POST',
        })
        .then(response => response.text())
        .then(message => console.log(message))
        .catch(error => console.error('Error:', error));
    }

