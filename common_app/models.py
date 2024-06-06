from django.db import models
from django.db.models import UniqueConstraint


# Create your api models here.

class ProjectInfo(models.Model):
    class Meta:
        db_table = 'project_info'
        verbose_name = '项目信息表'
        verbose_name_plural = '项目信息表'
        ordering = ('-project_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    project_name = models.CharField(max_length=90, unique=True)  # 项目名称, 不能为空, 不能重复
    project_desc = models.TextField(default="", null=True, blank=True)  # 项目描述, 可以为空, 默认为空字符串
    project_create_time = models.DateTimeField(auto_now_add=True)
    project_update_time = models.DateTimeField(auto_now=True)


class TestCase(models.Model):
    class Meta:
        db_table = 'testcase'
        verbose_name = '测试用例表'
        verbose_name_plural = '测试用例表'
        ordering = ('-case_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    project_id = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    case_id = models.CharField(default="", max_length=30, null=True, blank=True)  # 测试用例id, 冗余字段, 可以为空
    case_name = models.CharField(max_length=60, unique=True)  # 测试用例名称, 不能为空, 不能重复
    case_steps = models.JSONField(default=list, null=True, blank=True)  # 类似这样[{"key方法": "value参数"}]
    case_data = models.JSONField(default=list, null=True, blank=True)  # 冗余保存
    case_desc = models.TextField(default="", null=True, blank=True)  # 用例说明, 可以为空, 默认为空字符串
    case_ver = models.CharField(default="", max_length=30, null=True, blank=True)  # 用例版本, 可以为空, 默认空字符串
    case_create_time = models.DateTimeField(auto_now_add=True)
    case_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_name


class TestSuite(models.Model):
    class Meta:
        db_table = 'testsuite'
        verbose_name = '测试用例集'
        verbose_name_plural = '测试用例集'
        ordering = ('-suite_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    suite_name = models.CharField(max_length=60, unique=True)  # 测试用例集合名称, 不能为空, 不能重复
    suite_desc = models.TextField(default="", null=True, blank=True)  # 测试用例集合说明, 可以为空, 默认为空字符串
    suite_ver = models.CharField(default="", max_length=30, null=True, blank=True)  # 测试用例集合版本, 可以为空, 默认空字符串
    suite_create_time = models.DateTimeField(auto_now_add=True)
    suite_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.suite_name


class TestCaseRelateSuite(models.Model):
    class Meta:
        db_table = 'testcase_relate_testsuite'
        verbose_name = '测试用例和测试集关系表'
        verbose_name_plural = '测试用例和测试集关系表'
        ordering = ('-relate_create_time',)
        constraints = [
            # 指定组合唯一. 代表一个用例在同一个用例集中只能添加一次
            UniqueConstraint(fields=['case_p_id', 'suite_p_id'], name='unique_case_suite_combination')
        ]

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    case_p_id = models.ForeignKey(TestCase, on_delete=models.CASCADE)  # 关联用例主键,用例删除时,该记录删除
    suite_p_id = models.ForeignKey(TestSuite, on_delete=models.CASCADE)  # 关联用例集合主键,集合删除时,该记录删除
    relate_create_time = models.DateTimeField(auto_now_add=True)
    relate_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.suite_p_id) + ": " + str(self.case_p_id)


class TestTaskStatusAndReport(models.Model):
    class Meta:
        db_table = 'test_task_and_report'
        verbose_name = '测试任务和报告表'
        verbose_name_plural = '测试任务和报告表'
        ordering = ('-record_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    suite_p_id = models.ForeignKey(TestSuite, null=True, on_delete=models.SET_NULL)  # 当测试集被删除时, 此值置为Null
    # 对应的测试用例集合名称, 不能为空
    suite_name = models.CharField(max_length=60, verbose_name="对应的测试用例集名称", default="", null=True, blank=True)
    task_status = models.CharField(max_length=30, verbose_name="测试任务状态", default="Not Started", null=True,
                                   blank=True)
    report_path = models.TextField(verbose_name="测试报告路径", default="", null=True, blank=True)
    record_create_time = models.DateTimeField(auto_now_add=True)
    record_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.suite_name) + ": " + str(self.record_create_time)


class BusinessAction(models.Model):
    class Meta:
        db_table = 'business_action'
        verbose_name = '业务动作表'
        verbose_name_plural = '业务动作表'
        ordering = ('-action_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    project_p_id = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)  # 关联项目主键,项目删除时,该记录删除
    action_name = models.CharField(max_length=60, verbose_name="业务动作名称", unique=True)
    action_func = models.CharField(max_length=100, verbose_name="业务动作方法")
    action_desc = models.TextField(default="", null=True, blank=True)  # 业务动作说明, 可以为空, 默认为空字符串
    action_ver = models.CharField(default="", max_length=30, null=True, blank=True)  # 业务动作说版本, 可以为空, 默认空字符串
    action_create_time = models.DateTimeField(auto_now_add=True)
    action_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.action_name


class BusinessActionData(models.Model):
    class Meta:
        db_table = 'business_action_data'
        verbose_name = '业务动作数据表'
        verbose_name_plural = '业务动作数据表'
        ordering = ('-data_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    action_id = models.ForeignKey(BusinessAction, on_delete=models.CASCADE)  # 关联动作场景的主键,场景删除时,该记录删除
    data_name = models.CharField(max_length=60, verbose_name="业务数据名称")
    data_exp = models.JSONField(default=list, null=True, blank=True)  # 数据样例
    data_ver = models.CharField(default="", max_length=30, null=True, blank=True)  # 业务动作的版本, 可以为空, 默认空字符串
    data_create_time = models.DateTimeField(auto_now_add=True)
    data_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.data_name


class BusinessApi(models.Model):
    class Meta:
        db_table = 'business_api'
        verbose_name = '业务接口数据表'
        verbose_name_plural = '业务接口数据表'
        ordering = ('-api_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    project_id = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)  # 关联项目的主键,项目删除时,该记录删除
    api_name = models.CharField(max_length=100, unique=True)  # 接口名称,不能重复
    api_route = models.TextField()  # 接口路由(url)
    api_method = models.CharField(max_length=30)  # 接口Method
    api_data = models.JSONField(default=dict, null=True, blank=True)  # 接口post用到的 data数据模版(json)
    api_params = models.JSONField(default=dict, null=True, blank=True)  # 接口post用到的 params数据模版(json)
    api_route_params = models.JSONField(default=dict, null=True, blank=True)  # 接口组装route用到的 params数据模版(json)
    api_desc = models.TextField(default="", null=True, blank=True)  # 接口描述, 可以为空, 默认为空字符串
    api_ver = models.CharField(default="", max_length=30, null=True, blank=True)  # 业务动作版本, 可以为空, 默认空字符串
    api_create_time = models.DateTimeField(auto_now_add=True)
    api_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.api_name


class BusinessLocator(models.Model):
    class Meta:
        db_table = 'business_locator_table'
        verbose_name = '页面元素数据表'
        verbose_name_plural = '页面元素数据表'
        ordering = ('-locator_create_time',)

    id = models.AutoField(primary_key=True)  # 主动声明自增主键
    project_id = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)  # 关联项目的主键,项目删除时,该记录删除
    locator_name = models.CharField(max_length=100, unique=True)  # 页面元素名称,不能重复(因为要做映射)
    locator_selector = models.JSONField(default=list, null=True, blank=True)  # 类似这样[{"XPATH": "path"}]
    locator_desc = models.TextField(default="", null=True, blank=True)  # 页面元素描述, 可以为空, 默认为空字符串
    locator_ver = models.CharField(default="", max_length=30, null=True, blank=True)  # 页面元素版本, 可以为空, 默认空字符串
    locator_create_time = models.DateTimeField(auto_now_add=True)
    locator_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.locator_name
