from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listagem, name='listagem'),
    url(r'^pessoa/(?P<pk>[0-9]+)/$', views.detalhes, name='detalhes'),
    url(r'^cadastrar/nova_pessoa/$', views.cadastrarPessoa, name='cadastrarPessoa'),
    url(r'^pessoa/(?P<pk>[0-9]+)/cadastrar/novo_pertence/$', views.cadastrarPertences, name='cadastrarPertences'),
    url(r'^pessoa/(?P<pk>[0-9]+)/editar/$', views.editarPessoa, name='editarPessoa'),
    url(r'^pessoa/(?P<pk>[0-9]+)/excluir/$', views.excluir, name='excluir'),
]