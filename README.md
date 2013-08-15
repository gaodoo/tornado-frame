a frame work with tornado
=======

运行
==============
1) 安装mysql数据库
数据库用户名/密码 设为root/root, 或者修改core/database.py里 root:root为你的 用户名:密码

2) 连接mysql 建立 cgk数据库
mysql -u root -proot
create database cgk

3) 安装redis
ubuntu直接sudo apt-get instal redis-server
其他请自行谷歌

4) 安装python2.7及部分依赖库
sudo pip install tornado sqlalchemy wtforms selenium

5) 安装models
在项目根目录下，运行
python models.py

6) 运行测试服务器
python app.py

5) 浏览器访问
localhost:8000

验收测试
==============
先照上面运行起项目,
确定本地安装有最新firefox浏览器
项目根目录下运行
python fts.py

可访问url
======================
1)localhost:8000/   主页:未登录重定向到login, 或输出index page
2)localhost:8000/admin 后台主页，未登录冲定向到admin/login
3)localhost:8000/admin/login, 后台登录页
4)localhost:8000/login 注册/登录页



目前还有比较多问题
=====================
1)static_html目录下是写了一部分的静态html页面,可直接用浏览器打开,实现还比较粗糙，
2)因为整合功能测试和单元测试太难，所以代码写起来也比较费劲。
3)fts.py为功能测试(验收测试)代码,实现还较少
4)test.py为单元测试代码，实现还较少
5)models.py为数据建模部分
6)commands目录下为导入导出数据的两个工具，实现还比较简陋
