function csv_data(dataPath) {
    const request = new XMLHttpRequest(); // HTTPでファイルを読み込む
    request.addEventListener('load', (event) => { // ロードさせ実行
        const response = event.target.responseText; // 受け取ったテキストを返す
        csv_array(response); //csv_arrayの関数を実行
    });
    request.open('GET', dataPath, true); // csvのパスを指定
    request.send();
}

function csv_array(data) {
    const dataArray = []; //配列を用意
    const dataString = data.split('\n'); //改行で分割
    for (let i = 0; i < dataString.length; i++) { //あるだけループ
        dataArray[i] = dataString[i].split(',');
    }
    for (let i = 0; i < 15; i++)
    document.getElementById("aose"+i).innerHTML = '<div class="container" style="margin-top: 5%;"><h2 class="title" style="letter-spacing: normal; font-size: 130%; padding-top: 3%;"><a href="'+dataArray[i][3]+'"style="font-weight: bold;" id="aiseki1" target="_blank">' + dataArray[i][2] + '<i class="fas fa-map-marked-alt"></i></a></h2><div class="row justify-content-center"style="filter: drop-shadow(10px 10px 10px rgba(0,0,0,0.2)); border-radius: 10px; margin-right: 0; margin-left: 0;"><div class="col-6 text-center border-right"style="background: #d9f6ff; border-radius: 10px 0 0 10px;padding: 10%;"><h1 class="title" id="man1"><i class="fas fa-male" style="padding-right: 15%;"></i>'+ dataArray[i][0]+'</h1></div><div class="col-6 text-center border-right"style="background: #fdd8ed; padding: 0;border-radius: 0px 10px 10px 0px; padding: 10%;"><h1 class="title" id="woman1"><i class="fas fa-male" style="padding-right: 15%;"></i>'+dataArray[i][1]+'</h1></div></div></div>'

}
csv_data('results.csv');