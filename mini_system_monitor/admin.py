import os
import psutil
import datetime
import platform

from django.contrib import admin
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
from django.conf import settings
import django

from .models import Settings, Env, Overview


class ViewOnlyAmin(admin.ModelAdmin):
    def get_actions(self, request):
        return None

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


def get_all_settings():
    if not settings.configured:
        settings.configure()
    dict_settings = settings.__dict__.copy()
    
    if '_wrapped' in dict_settings: del dict_settings['_wrapped']
    if 'is_overridden' in dict_settings: del dict_settings['is_overridden']

    from collections import OrderedDict
    return OrderedDict(sorted(dict_settings.items()))


@admin.register(Settings)
class SettingsAdmin(ViewOnlyAmin):
    view_on_site = False
    change_list_template = 'admin/settings_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if request.user.is_superuser:
            response.context_data['settings'] = get_all_settings()
        return response



def get_all_envs():
    envs = dict(os.environ)
    envs = dict(sorted(envs.items(), key=lambda item: item[0]))
    return envs

@admin.register(Env)
class EnvAdmin(ViewOnlyAmin):
    view_on_site = False
    change_list_template = 'admin/env_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if request.user.is_superuser:
            response.context_data['envs'] = get_all_envs()
        return response


def get_overview():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    root_disk = psutil.disk_usage('/')
    return [
        {
            'name': 'cpu_percent',
            'value': psutil.cpu_percent(interval=1),
        },
        {
            'name': 'memory_percent',
            'value': memory.percent
        },
        {
            'name': 'swap_percent',
            'value': swap.percent
        },
        {
            'name': 'root_disk_percent',
            'value': root_disk.percent
        }
    ]

def get_static_overview():
    uname = platform.uname()
    return [
        {
            'name': 'hostname', 
            'value': platform.node()
        },
        {
            'name': 'os_uname',
            'value': f'{uname.system} - {uname.release}  - {uname.machine} - {uname.processor}'
        },
        {
            'name': 'boot_time',
            'value': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            'name': 'cpu_count',
            'value': psutil.cpu_count()
        },
        {
            'name': 'python_version', 
            'value': platform.python_version()
        },
        {
            'name': 'django_version', 
            'value': django.get_version()
        },

    ]


@admin.register(Overview)
class OverviewAdmin(ViewOnlyAmin):
    view_on_site = False
    change_list_template = 'admin/overview_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('api.json/', self.api),
        ]
        return custom_urls + urls

    def api(self, request):
        response = JsonResponse(get_overview(), safe=False)
        return response

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if request.user.is_superuser:
            if hasattr(response, 'context_data'):
                response.context_data['data'] = get_overview()
                response.context_data['static_overview'] = get_static_overview()
        return response

    class Media:
        js = (
            'mini_system_monitor/js/gridjs.js',
            'mini_system_monitor/js/index.js',
        )
        css = ('mini_system_monitor/css/mermaid.css',)