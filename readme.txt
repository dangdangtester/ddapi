解决github访问超时：
登录https://github.com.ipaddress.com/www.github.com 查看当前github.com对应的IP地址
按以上查询信息修改host
打开cmd，输入    ipconfig/flushdns  回车即可

更新日志：
20220322
-修改了send_mail.py文件中的默认的发送服务器账号，大家可以配置自己的账号
-新增了执行testcase目录下多个excel文件功能，方便大家管理测试用例（一个excel对应一个系统或者一个excel对应一个接口都可以）
