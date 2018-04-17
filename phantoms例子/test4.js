
system=require('system');
url = system.args[1];

var page = require('webpage').create();

page.open(url, function(status) {
  if(status === "success"){
            // 处理页面
          var pic_url = page.evaluate(function() {
            // DOM操作
            return document.getElementById('banner_link').getAttribute('class');
          });
          console.log(pic_url);
  }else{
    console.log('failed');
  }
  phantom.exit();
});

