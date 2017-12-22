#模板引擎,页面上重复的HTML部分的复用问题

#uikit是一个强大的CSS框架，可以下载利用

#<html>
#    <% include file="inc_header.html" %>
#    <% include file="index_body.html" %>
#    <% include file="inc_footer.html" %>
#</html>

#模板可继承应用
#父模板  block:可替换的内容
'''
<!-- base.html -->
<html>
    <head>
        <title>{% block title%} 这里定义了一个名为title的block {% endblock %}</title>
    </head>
    <body>
        {% block content %} 这里定义了一个名为content的block {% endblock %}
    </body>
</html>
'''

#子模板
'''
{% extends 'base.html' %}

{% block title %} A {% endblock %}

{% block content %}
    <h1>Chapter A</h1>
    <p>blablabla...</p>
{% endblock %}
'''