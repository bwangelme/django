#!/usr/bin/env python3
# -*- coding: utf-8 -*-"

"""
问题说明：

uwsgi 执行 importlib.import_module 函数的行为和 Python 执行的不同。

问题复现的方法:

    uwsgi: > uwsgi --http :9090 --wsgi-file app.py
           > http :9090/url_input                                               21:02:58 (03-29)
           HTTP/1.1 200 OK
           Content-Length: 117
           Content-Type: text/plain

           module __path__ is: _NamespacePath(['./module', '/Users/michaeltsui/Bundle/django/django/demo/import_module/module'])

    python: > python app.py
            module __path__ is: _NamespacePath(['/Users/michaeltsui/Bundle/django/django/demo/import_module/module'])
"""


import importlib


def get_module_path():
    mod = importlib.import_module("module")

    if not hasattr(mod, "path"):
        paths = getattr(mod, "__path__")
        return "module __path__ is: {}".format(paths)


def application(env, start_response):
    response_body = "{}".format(
            get_module_path()
    )
    response_body = response_body.encode()

    status = '200 OK'

    response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)

    return [response_body]


if __name__ == '__main__':
    print(get_module_path())
