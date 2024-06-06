from django.contrib import admin

# Register your models here.

from common_app.models import ProjectInfo, TestCase, TestSuite, TestCaseRelateSuite
from common_app.models import TestTaskStatusAndReport, BusinessAction, BusinessActionData
from common_app.models import BusinessLocator, BusinessApi


class ProjectInfoAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = ('id', 'project_name', 'project_desc', 'project_create_time', 'project_update_time')
    # 定义web上可编辑的字段
    list_editable = ('project_name', 'project_desc')
    # 定义web上可被搜索的字段
    search_fields = ('project_name',)
    # 定义web上可过滤的字段
    list_filter = ()

    ordering = ('-project_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class TestCaseAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = ('id', 'project_id', 'case_id', 'case_name', 'case_steps', 'case_data', 'case_desc', 'case_ver',
                    'case_create_time', 'case_update_time',)
    # 定义web上可编辑的字段
    list_editable = ('case_id', 'case_name', 'case_steps', 'case_data', 'case_desc', 'case_ver')
    # 定义web上可被搜索的字段
    search_fields = ('project_id', 'case_id', 'case_name', 'case_ver')
    # 定义web上可过滤的字段
    list_filter = ('case_ver', 'project_id',)

    ordering = ('-case_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class TestSuiteAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = ('id', 'suite_name', 'suite_desc', 'suite_ver', 'suite_create_time', 'suite_update_time')
    # 定义web上可编辑的字段
    list_editable = ('suite_name', 'suite_desc', 'suite_ver')
    # 定义web上可被搜索的字段
    search_fields = ('suite_name', 'suite_ver')
    # 定义web上可过滤的字段
    list_filter = ('suite_ver',)

    ordering = ('-suite_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class TestCaseRelateSuiteAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = ('id', 'case_p_id', 'suite_p_id', 'relate_create_time', 'relate_update_time')
    # 定义web上可编辑的字段
    list_editable = ()
    # 定义web上可被搜索的字段
    search_fields = ('case_p_id', 'suite_p_id')
    # 定义web上可过滤的字段
    list_filter = ('case_p_id', 'suite_p_id')

    ordering = ('-relate_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class TestTaskStatusAndReportAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = (
    'id', 'suite_p_id', 'suite_name', 'task_status', 'report_path', 'record_create_time', 'record_update_time')
    # 定义web上可编辑的字段
    list_editable = ('suite_name', 'task_status', 'report_path')
    # 定义web上可被搜索的字段
    search_fields = ('suite_name', 'task_status')
    # 定义web上可过滤的字段
    list_filter = ('suite_p_id', 'task_status')

    ordering = ('-record_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class BusinessActionAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = (
        'id', 'project_p_id', 'action_name', 'action_func', 'action_desc', 'action_ver', 'action_create_time',
        'action_update_time')
    # 定义web上可编辑的字段
    list_editable = ('action_name', 'action_func', 'action_desc', 'action_ver')
    # 定义web上可被搜索的字段
    search_fields = ('action_name', 'action_func', 'action_ver')
    # 定义web上可过滤的字段
    list_filter = ('action_ver', 'project_p_id')

    ordering = ('-action_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class BusinessActionDataAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = ('id', 'action_id', 'data_name', 'data_exp', 'data_ver', 'data_create_time', 'data_update_time')
    # 定义web上可编辑的字段
    list_editable = ('data_name', 'data_exp', 'data_ver')
    # 定义web上可被搜索的字段
    search_fields = ('action_id', 'data_name', 'data_ver')
    # 定义web上可过滤的字段
    list_filter = ('action_id', 'data_ver')

    ordering = ('-data_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class BusinessApiAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = (
    'id', 'project_id', 'api_name', 'api_route', 'api_method', 'api_data', 'api_params', 'api_route_params',
    'api_desc', 'api_ver', 'api_create_time', 'api_update_time')
    # 定义web上可编辑的字段
    list_editable = (
    'api_name', 'api_route', 'api_method', 'api_data', 'api_params', 'api_ver', 'api_route_params', 'api_desc')
    # 定义web上可被搜索的字段
    search_fields = (
    'api_name', 'api_route', 'api_method', 'api_data', 'api_params', 'api_ver', 'api_route_params', 'api_desc')
    # 定义web上可过滤的字段
    list_filter = ('api_method', 'api_ver', 'project_id')

    ordering = ('-api_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


class BusinessLocatorAdmin(admin.ModelAdmin):
    # 定义web上显示的字段
    list_display = (
        'id', 'project_id', 'locator_name', 'locator_selector', 'locator_desc', 'locator_ver', 'locator_create_time',
        'locator_update_time')
    # 定义web上可编辑的字段
    list_editable = ('locator_name', 'locator_selector', 'locator_desc', 'locator_ver')
    # 定义web上可被搜索的字段
    search_fields = ('locator_name', 'project_id', 'locator_ver')
    # 定义web上可过滤的字段
    list_filter = ('project_id', 'locator_ver')

    ordering = ('-locator_create_time',)  # 页面用api_create_time倒序排序（最新的在最前面）
    actions_on_top = True  # 在顶部栏显示操作
    actions_on_bottom = False  # 关闭底部栏的显示操作


admin.site.register(ProjectInfo, ProjectInfoAdmin)
admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestSuite, TestSuiteAdmin)
admin.site.register(TestCaseRelateSuite, TestCaseRelateSuiteAdmin)
admin.site.register(TestTaskStatusAndReport, TestTaskStatusAndReportAdmin)
admin.site.register(BusinessAction, BusinessActionAdmin)
admin.site.register(BusinessActionData, BusinessActionDataAdmin)
admin.site.register(BusinessLocator, BusinessLocatorAdmin)
admin.site.register(BusinessApi, BusinessApiAdmin)  # 注册要管理的数据表
