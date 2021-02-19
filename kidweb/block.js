
  var weblists= {
    "初中化学视频":"https://www.bilibili.com/video/BV1ux411f7dB",  
    "初中物理视频":"https://www.bilibili.com/video/BV12s41177kT",
    "初中数学视频":"https://www.bilibili.com/video/BV1qb411A7Zz",
    "初中英语视频":"https://www.bilibili.com/video/BV1ca4y1e7we",
    "八下历史视频":"https://www.bilibili.com/video/BV1aA411J7gZ",
    "英语音标":"https://www.bilibili.com/video/BV1iV411z7Nj",
    "马丁物理":"https://www.bilibili.com/video/BV12K4y1W75r",
    "生物重点内容中考复习":"https://www.bilibili.com/video/BV1n7411T79k",
    //"dota2_pa":"https://www.bilibili.com/video/BV1Kt4y1C7eB",
}
function makeButtons() {
    
    var ButtonsDiv =document.getElementById("buttons"); 
    for(var webname in weblists){
      var bt =document.createElement("button");           //createElement生成button对象
      bt.innerText = webname; 
      bt.id=webname;
      bt.onclick=function(){
        window.location.href=weblists[this.id];
        return false;
      };
      
      
      ButtonsDiv.appendChild(bt)
  }
           
 }


module.exports  ={
  valid:function validate(url){
    for(var webname in weblists){
        if(url == weblists[webname]){
          return true;
        } 
    }
    return false;
  },
}
