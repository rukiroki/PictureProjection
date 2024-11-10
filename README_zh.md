PictureProjection 是一款可以将图片转换成我的世界基岩版投影的简单程序，搭配Spritecraft地图画生成工具使用: [Spritecraft](https://autosaved.org/Spritecraft)\
此程序会生成一个基岩版材质包文件`.mcpack`，基于盔甲夹实体的投影显示。更多请看*快速上手*

## 特点
- 当前版本只支持最大128*128个方块的平面地图画图片投影制作
- 不需要图片是完全正方形的
- 盔甲架投影
- 消耗命名牌

## 快速上手 && 沉浸式教程
### 首先你需要下载发布版本 [Release 0.1.0](https://github.com/rukiroki/PictureProjection/releases/tag/0.1.0) 中的第一个压缩包。
![image](https://github.com/user-attachments/assets/bb6d98ae-4de5-44f3-bf45-35961acb0820)
### 然后解压压缩包到一个目录。
![image](https://github.com/user-attachments/assets/b3defbc4-69d3-4f6f-8dad-1517d21cfd90)
### 双击打开程序`Picture Projection.exe`会弹出两个窗口。
![image](https://github.com/user-attachments/assets/47a554c7-b1bf-488b-a8a9-064e5cdc72a9)
### 在网页上生成地图画
复制命令行窗口中的链接 [Spritecraft](https://autosaved.org/Spritecraft) 到浏览器打开，生成您的地图画。注意，当前版本最大支持128*128。
1. 设置最大宽高为128，128。
2. 选择你想要转换成地图画的图片。
3. 选择你想要的方块。
4. 点击"生成像素画"按钮。
5. 点击"下载图像"按钮，下载生成好的图像。

![image](https://github.com/user-attachments/assets/848128fb-8862-4acc-939a-17e470748f39)![image](https://github.com/user-attachments/assets/b5b9f199-1eb2-42f6-9b4c-c39de3ad6bd6)
### 到选择图片窗口选择你刚才生成好并下载的图片。
![image](https://github.com/user-attachments/assets/1a370688-8aa3-479b-81a0-bc0233a1afba)
### 点击确定，开始转换，转换完成后程序会自动关闭。生成的文件会放在程序根目录下
![image](https://github.com/user-attachments/assets/70346e99-157d-4aa4-8c40-826ea8705005)
### 双击打开文件`Picture projection.mcpack`，会自动导入资源包，在世界或者全局激活资源包。
> 资源包不会改变游戏行为和规则，全局激活即可在服务器中使用。

![image](https://github.com/user-attachments/assets/73152154-e7f2-4014-952e-9dd271a540a6)
![image](https://github.com/user-attachments/assets/c583a6b5-d3e1-462e-aa89-43f68ffd4a50)
### 定位地图画建造位置
加入世界，拿出盔甲夹，铁砧，命名牌，地图，显眼的标记方块（如红石块）
用铁砧分别命名命4个名牌为：p01，p02.p03，p04，因为地图画被分成了4部分，否则由于基岩版实体渲染范围只有70格，距离盔甲架比较远的话会不显示。\
拿出地图，配合显眼的标记方块找到地图的左下角，把盔甲架放在地图的左下角再往左一格下一格的地方（定义地图的上下左右为上下左右）。
![image](https://github.com/user-attachments/assets/2032402f-780e-4d5c-aabd-82c62acf8083)
### 定位四个盔甲架所放置的位置
本材质包的盔甲架后方32格和左方32格以及左后方32，32（对于地图来说是上和右）的地方各有一个用来标记的小木棍，是用来方便找到4个盔甲架放置的位置的。
![image](https://github.com/user-attachments/assets/c10ce13d-ed7e-411b-9e70-3044d85dfd62)
在坐标（上图自定义）-1，-1的盔甲架（-1）的位于对角32，32的木棍上面向地图上方放一个盔甲架（0），在这个盔甲架的三个木棍上分别向着地图上方放置三个盔甲架，然后在位于位于上的盔甲架的上木棍朝下放置一个盔甲架（1），在位于对角上的盔甲架的对角木棍上朝下放置一个盔甲架（2），在位于右方的盔甲架右木棍上朝下放置一个盔甲架（3）。
![4775d2fa6433b977efd79a867838775b](https://github.com/user-attachments/assets/3c06c51b-0913-49ad-a8d0-7f807f47adbd)

### 为盔甲架命名 && 展示图像
把（0）号盔甲架的朝向改成向下。拿出预备好的4个命名牌，为（1）号盔甲架命名"p01"，为（2）号盔甲架命名"p02"，为（3）号盔甲架命名"p04"，为（0）号盔甲架命名"p03"，图像投影就会在盔甲架周围显示出来。
![image](https://github.com/user-attachments/assets/a1aa6702-343e-4011-99d0-f16247a43ff1)
### 大功告成
现在地图画的投影以80%的不透明度显示在世界里，准备好所需的建筑材料就可以开始着手建造了。
![image](https://github.com/user-attachments/assets/e55d28d2-0fce-46fb-8889-4d81f8f55d88)
在本例中，图片不是正方形。如果你导入的图片不是正方形，投影会倾向于靠左上显示。
