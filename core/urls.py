from django.urls import path, re_path, include
from .views import (
	home, 
	lista_pessoas, 
	lista_veiculos, 
	lista_movrotativos,
	lista_mensalistas,
	lista_movmensalistas,
	pessoa_novo,
	veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativos_update,
    mensalista_update,
    movmensalista_update,
)

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    
    re_path(r'^mov-rot/$', lista_movrotativos, name='core_lista_movrotativos'),
    re_path(r'^mov-rot-novo/$', movrotativos_novo, name='core_movrotativos_novo'),
    re_path(r'^mov-rot-update/(?P<id>\d+)/$', movrotativos_update, name='core_movrotativo_update'),
    
    re_path(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    re_path(r'^mensalistas-novo/$', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    
    re_path(r'^mov-mensal-novo/$', movmensalista_novo, name='core_movmensalista_novo'),
    re_path(r'^mov-mensal/$', lista_movmensalistas, name='core_lista_movmensalistas'),
    re_path(r'^mov-mensal-update/(?P<id>\d+)/$', movmensalista_update, name='core_movmensalista_update'),
]
