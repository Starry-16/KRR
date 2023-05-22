#### 安装教程

1.  安装python包：requirements.txt
~~~
pip install -r requirements.txt
~~~
2.  model模型在群文件里ltp_data_v3.4.0，把文件解压，并且把里面的.model文件放到kg\model文件夹下。也可以[点击这里](http://ltp.ai/download.html)下载ltp_data_v3.4.0.zip，但是需要把里面的pisrl.model换成[这里](http://model.scir.yunfutech.com/server/3.4.0/pisrl_win.model)的pisrl_win.model



#### 使用说明

1.  test文件是我测试代码的文件，不用管
2.  .gitattributes是避免上传代码Linux和windows换行符的问题，不用管
3.  triple_extraction里面是分词和事件提取还有数据处理
4.  reptil是简单的爬虫代码
5.  语义标注模型应该用windows版本的（pisrl_win.model），但是经过摸索我发现提取的差别为0，可能是本项目数据集过于简单的原因。运行本项目可以选择使用第一个快的，加载一个空模型（文件夹内不能有pisrl.model文件）

![1](https://github.com/Starry-16/KRR/assets/89348402/1cb03a6d-897c-4c6f-9f4b-6e302a76ed37)

6.  11
7.  






