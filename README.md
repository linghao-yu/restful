# restful
Todo list

使用node框架，构建一个Restful API，能够完成Todo list的以下功能。

    返回所有Todo任务
    创建一个新的Todo任务
    返回一个指定ID的Todo任务
    删除一个Todo任务

为简化流程，不引入数据存储，即，不需要做数据持久化，可以在服务器运行时满足功能即可。

Todo中一个任务的JSON格式定义为：

  {
    "id": 1,
    "content": "Restful API homework",
    "createdTime": "2019-05-15T00:00:00Z"
  }
