from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#注册模型，
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    list_display = ['gname','gdate','ggirlnum','gboynum','isDelete']
    #列表页属性
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 10
    # 添加修改页属性
    fieldsets = [
        ('num',{'fields':['ggirlnum','gboynum']}),
        ('base',{'fields':['gname','gdate','isDelete']}),
    ]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 10
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True









