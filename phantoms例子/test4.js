
system=require('system');
url = system.args[1];

var page = require('webpage').create();

page.open(url, function(status) {
  if(status === "success"){
            // ����ҳ��
          var pic_url = page.evaluate(function() {
            // DOM����
            return document.getElementById('banner_link').getAttribute('class');
          });
          console.log(pic_url);
  }else{
    console.log('failed');
  }
  phantom.exit();
});

