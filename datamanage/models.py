from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
对于任务具有如下属性：
1、任务名称
2、任务简述 -- 一段文字
3、任务详情 -- mkdown语法
4、任务开始日期
5、任务结束日期
6、任务开始时间
7、任务结束时间
8、是否重复任务
9、任务时间节点
10、任务状态 - 是否完成、正在进行中，正在进行即是到当前日期 0完成1未完成2进行中
11、剩余时间 - 仅当任务状态处于正在进行中时进行计算
12、任务工作地点
13、任务交付内容
14、任务交付对象
15、uuid
16、创建日期
17、更新日期
18、创建人 - 即改任务属于哪一个用户
"""


class TasksModel(models.Model):
    uuid = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks_name = models.CharField(max_length=150)
    tasks_decs = models.TextField()
    tasks_detail = models.TextField()
    tasks_start_date = models.DateField()
    tasks_end_date = models.DateField()
    tasks_start_time = models.TimeField()
    tasks_end_time = models.TimeField()
    tasks_continued = models.CharField(max_length=50)
    is_task_repeat = models.BooleanField(default=False)
    tasks_status = models.IntegerField(default=1)
    tasks_time_node = models.DateTimeField(blank=True, null=True)
    left_time = models.IntegerField(default=0)
    task_location = models.CharField(max_length=150)
    task_deliver_content = models.CharField(max_length=150)
    task_deliver_object = models.CharField(max_length=150)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uuid
