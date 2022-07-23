# xuexitong_auto_play
超星学习通自动刷课
更新于2022/7/23
## Q:程序能做什么？
A:自动刷视频课，自动阅读文档
## Q:程序工作原理？
A:程序调用pyautogui模块，以图像识别的方式模拟人工刷课。程序只模拟鼠标运动，无快进功能，所以无法缩减时间成本。
## Q:为什么用这种方式完成任务？
A:网传学习通的检测比较严格，说法也是林林总总，真假难辨。脚本一键刷课后台可能会有不良记录，用图像识别模拟人工似乎是比较保险的方法。当然，还有一个很现实的原因，我只会这个.....  
<img src="https://user-images.githubusercontent.com/53106447/180587779-c42a8820-5e18-4c38-a06b-cc831de8170b.png" width="200" height="200" alt="微信小程序"/><br/>
## Q:如何使用？
1.使用请配置python编译环境，并安装pyautogui模块（新增confidence参数须安装opencv模块，如遇安装困难，可手动删除confidence参数，但适用性会因此降低）  
2.将待匹配图标的png文件置于autogui.py的同一目录下，如图所示：
![目录图](https://user-images.githubusercontent.com/53106447/180586990-bc600d75-ecb8-44a0-b216-38f2e3767905.png)
## Tip：png文件可视情况自行调整，图标文件画幅过小或特征不明显则可能无法识别或错误识别
3.使用终端指令或在Pycharm、vscode等编译器运行
## 注意
1.程序运行时最大化网页窗口，以便定位与匹配目标项  
2.debug全程使用1920*1080分辨率的机器、Windows系统的Edge浏览器，无dark模式，默认字体字号，无缩放。程序中许多语句是与分辨率和缩放比例高度绑定的，个性化的设置可能会导致程序运行时出错  
例如：程序未写入屏幕中同时出现多个与undone.png匹配的处理办法，此类情况在特殊缩放比例与分辨率高于1080的屏幕中可能出现  
3.Mac和Linux发行版因字体、字号、缩放比例等差异可能会导致错误，可视情况调整png文件与定位参数  
附效果图：  
![image](https://user-images.githubusercontent.com/53106447/180587684-9ecb0172-4022-4892-b6b0-685ebb912d99.png)
4.程序运行时机器应处于闲置状态，勿操作其他事项
