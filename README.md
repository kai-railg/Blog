# Blog
分布式个人博客系统
此项目后端使用 django + beego 框架，前端使用 bs+layui 编写，由 nginx 代理和负载均衡。

django 框架中又实现了注册功能的拆分和独立部署。

此项目旨在完成项目从服务层面的解耦。一方面独立的功能各司其职，互不干扰，一方面功能实现上的代码也“各凭心意“。

通过此项目你可以了解到：

- 分布式项目的具体实现
- Django 高级 api 的使用
- Django 后台管理功能的挖掘
- go 语言的特点和 beego 框架的灵巧性
- shell 脚本对 nginx 日志的切分
- 基于 docker 的自动化部署流程

此项目下一步的目标：
- RabbitMQ 消息中间件
- 越来越多的 go 语言功能
- DockerHub 的 WebHook 持续集成

项目文档在我的 Notio 笔记中，<a href="https://www.notion.so/ArchMD-81a72022dab04716a2b5f55705dfaa9b">查看</a>。


