$(function() {                          //カレンダーで日にち引っ張ってくるやつ(from)
            var path="./img/dom/"+get_today()+".jpg"
            var img=document.getElementById("kondate");
            img.src=path;
//            console.log(get_today());
//            console.log(path);
});

function get_today(){         //英語の意味通り
  var myd= new Date();
  var year  = myd.getFullYear();
  var month = myd.getMonth()+1;
  var date  = myd.getDate();
  if(month<10) month='0'+month;
  if(date<10)date='0'+date;
  var str = String(year) + String(month) + String(date) ;
  return str;
}
