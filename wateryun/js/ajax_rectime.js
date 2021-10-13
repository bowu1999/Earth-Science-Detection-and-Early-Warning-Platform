// (setTimeout(function(){
//   var xmlhttp;
//   if (window.XMLHttpRequest){
//     // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
//     xmlhttp=new XMLHttpRequest();
//   }
//   else{
//     // IE6, IE5 浏览器执行代码
//     xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
//   }
//   xmlhttp.open("POST","http://123.56.91.110/wateryun/readdata.php",true);
//   // xmlhttp.open("POST","../readdata.php",true);
//   xmlhttp.send();
//   xmlhttp.onload=function(){
//     if (xmlhttp.readyState==4 && xmlhttp.status==200){
//       var strlist = xmlhttp.responseText.split(" ");
//       var idx = 0;
//       for(var i=0;i<7;i++){
//         var sp = 'sp'+ i+'_';
//         for(var j=0;j<8;j++){
//           var p_s = sp + j;
//           console.log(p_s);
//           console.log(idx);
//           var sp_ = document.getElementById(p_s);
//           sp_.innerHTML=strlist[idx++];
//         }
//       }
//     }
//   }
// },1000))();
var xmlhttp;
function createXMLHttpRequest(){
  if (window.XMLHttpRequest){
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else{
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
}
function Autofresh(){
  createXMLHttpRequest();    
  xmlhttp.open("POST","http://123.56.91.110/wateryun/readdata.php",true);
  // xmlhttp.open("POST","../readdata.php",true);
  xmlhttp.onreadystatechange=doAjax;
  xmlhttp.send();
}
function doAjax(){
  if (xmlhttp.readyState==4 && xmlhttp.status==200){
      var strlist = xmlhttp.responseText.split(" ");
      var idx = 0;
      for(var i=0;i<7;i++){
        var sp = 'sp'+ i+'_';
        for(var j=0;j<8;j++){
          var p_s = sp + j;
          console.log(p_s);
          console.log(idx);
          var sp_ = document.getElementById(p_s);
          sp_.innerHTML=strlist[idx++];
        }
      }
      setTimeout("Autofresh()",2000);
    }
}
Autofresh()