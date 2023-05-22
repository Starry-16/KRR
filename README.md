#### 安装教程


1.  安装python包：requirements.txt
~~~
pip install -r requirements.txt
~~~
2.  model模型在群文件里ltp_data_v3.4.0，把文件解压，并且把里面的.model文件放到kg\model文件夹下。也可以[点击这里](http://ltp.ai/download.html)下载ltp_data_v3.4.0.zip，但是需要把里面的pisrl.model换成[这里](http://model.scir.yunfutech.com/server/3.4.0/pisrl_win.model)的pisrl_win.model


#### 使用说明

1.  test文件是我测试代码的文件，不用管
2.  .gitattributes是避免上传代码Linux核windows换行符的问题，不用管
3.  triple_extraction里面是分词和事件提取还有数据处理
4.  reptil是简单的爬虫代码
