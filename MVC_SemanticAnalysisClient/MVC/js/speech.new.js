/** 麥克風按鈕 */
const microphoneButton = document.getElementById('mic_button');

/** 麥克風按鈕圖片 */
const microphoneButtonImage = document.getElementById('mic');

/** 語音識別結果顯示 */
const messagesDiv = document.getElementById('cube');

/** 語音識別 */
const speechRecognition = new webkitSpeechRecognition();

/** API網址 */
const apiUrl = (
  // 'https://cors-anywhere.herokuapp.com/' +
  'https://itri.dasgo.com.tw:5002/webhooks/rest/webhook'
);

speechRecognition.continuous = false;
speechRecognition.lang = "cmn-Hant-TW";

main();

/** 主程式 */
async function main() {
  while (true) {
    /** 語音辨識結果 */
    const message = await whenSpeechRecognitionGotResult();

    insertMessageDivInMessagesDiv(message.replace(/\s*/g,""));

    try {
      const response = await whenApiRequestGotResponse(message.replace(/\s*/g,""));

      //const [{ text: apiMessage }] = await response.json();
      const apiMessages  = await response.json();

      for (const apiMessage of apiMessages){
         insertMessageDivInMessagesDivReply(apiMessage.text);
      }
      //console.log("apiMessageLen: ",apiMessage.length)
      //insertMessageDivInMessagesDivReply(apiMessage);

    } catch(error) {
      console.log(error);
    }
  }
}

/** 建立訊息顯示 */
function insertMessageDivInMessagesDiv(message) {
  const messageDiv = document.createElement('div');
  messageDiv.className = 'cube';

  messageDiv.innerText = message;
  messagesDiv.appendChild(messageDiv);
  $('#talk').scrollTop($('#talk').height());
}

function insertMessageDivInMessagesDivReply(message) {
  const messageDiv = document.createElement('div');
  messageDiv.className = 'cubereply';

  messageDiv.innerText = message;
  messagesDiv.appendChild(messageDiv);
  $('#talk').scrollTop($('#talk').height());
}

/** 當API請求得到回應 */
function whenApiRequestGotResponse(message) {
  console.log(message);
  return fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      sender: 'user',
      message,
    }),
  });
}

/** 當麥克風按鈕按下 */
function whenMicrophoneButtonMouseDown() {
  return new Promise((callbackWhenButtonMouseDown) => {
    microphoneButton.onmousedown = callbackWhenButtonMouseDown;
  });
}

/** 當麥克風按鈕放開 */
function whenMicrophoneButtonMouseUp() {
  return new Promise((callbackWhenButtonMouseUp) => {
    microphoneButton.onmouseup = callbackWhenButtonMouseUp;
  });
}

/** 當語音辨識結束 */
function whenSpeechRecognitionEnd() {
  return new Promise((callbackWhenSpeechRecognitionEnd) => {
    speechRecognition.onend = callbackWhenSpeechRecognitionEnd;
  });
}

/** 當語音辨識得到結果 */
function whenSpeechRecognitionGotResult() {
  return new Promise(async (callbackWhenSpeechRecognitionGotResult) => {
    /** 語音辨識結果 */
    let speechRecognitionResult = '';

    await whenMicrophoneButtonMouseDown();
    microphoneButtonImage.src = 'MVC/Image/mic_use.png';

    speechRecognition.onresult = ({ resultIndex, results }) => {
      speechRecognitionResult = results[resultIndex][results.length - 1].transcript;
    };

    speechRecognition.start();

    // 等待放開按鈕且辨識完成
    await Promise.all([
      whenMicrophoneButtonMouseUp(),
      whenSpeechRecognitionEnd(),
    ]);

    microphoneButtonImage.src = 'MVC/Image/mic.png';
    callbackWhenSpeechRecognitionGotResult(speechRecognitionResult);
  });
}

async function textinput() {
    const textdata = document.getElementById('textarea');
    const message = textdata.value
    insertMessageDivInMessagesDiv(message.replace(/\s*/g,""));
    try {
        response = await whenApiRequestGotResponse(message.replace(/\s*/g,""));
        //response = whenApiRequestGotResponse(textdata.value);
        //[{ text: apiMessage }] = response.json();

        //insertMessageDivInMessagesDiv(apiMessage);
        const apiMessages  = await response.json();

        for (const apiMessage of apiMessages){
            insertMessageDivInMessagesDivReply(apiMessage.text);
        }
      } catch(error) {
        console.log(error);
      }
}
