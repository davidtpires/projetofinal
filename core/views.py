from django.shortcuts import render, redirect
from .models import (
	Pessoa, 
	Veiculo, 
	MovRotativo,
	Mensalista,
	MovMensalista,
)

from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm

def home(request):
	context = {'mensagem': 'Ola mundo'}
	return render(request, 'core/index.html', context)


def lista_pessoas(request):
	pessoas = Pessoa.objects.all()
	form = PessoaForm()
	data = {'pessoas': pessoas, 'form': form}
	return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
	form = PessoaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_pessoas')

def pessoa_update(request, id):
	data = {}
	pessoa = Pessoa.objects.get(id=id)
	form = PessoaForm(request.POST or None, instance=pessoa)
	data['pessoa'] = pessoa
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_pessoas')
	else:
		return render(request, 'core/update_pessoa.html', data)


def veiculo_novo(request):
	form = VeiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_veiculos')


def lista_veiculos(request):
	veiculos = Veiculo.objects.all()
	form = VeiculoForm()
	data = {'veiculos': veiculos, 'form': form}
	return render(request, 'core/lista_veiculos.html', data)


def veiculo_update(request, id):
	data = {}
	veiculo = Veiculo.objects.get(id=id)
	form = VeiculoForm(request.POST or None, instance=veiculo)
	data['veiculo'] = veiculo
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_veiculos')
	else:
		return render(request, 'core/update_veiculo.html', data)


def lista_movrotativos(request):
	mov_rot = MovRotativo.objects.all()
	form = MovRotativoForm()
	data = {'mov_rot': mov_rot, 'form': form}
	return render(request, 'core/lista_movrotativos.html', data)


def movrotativos_novo(request):
	form = MovRotativoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_movrotativos')


def movrotativos_update(request, id):
	data = {}
	mov_rotativo = MovRotativo.objects.get(id=id)
	form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
	data['mov_rotativo'] = mov_rotativo
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_movrotativos')
	else:
		return render(request, 'core/update_movrotativo.html', data)

def lista_mensalistas(request):
	mensalistas = Mensalista.objects.all()
	form = MensalistaForm()
	data = {'mensalistas': mensalistas, 'form': form}
	return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
	form = MensalistaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_mensalistas')


def mensalista_update(request, id):
	data = {}
	mensalista = Mensalista.objects.get(id=id)
	form = MensalistaForm(request.POST or None, instance=mensalista)
	data['mensalista'] = mensalista
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_mensalistas')
	else:
		return render(request, 'core/update_mensalista.html', data)


def lista_movmensalistas(request):
	mov_mensalistas = MovMensalista.objects.all()
	form = MovMensalistaForm()
	data = {'mov_mensalistas': mov_mensalistas, 'form': form}
	return render(request, 'core/lista_movmensalistas.html', data)


def movmensalista_novo(request):
	form = MovMensalistaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_movmensalistas')


def movmensalista_update(request, id):
	data = {}
	mov_mensalista = MovMensalista.objects.get(id=id)
	form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
	data['mov_mensalista'] = mov_mensalista
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_movmensalistas')
	else:
		return render(request, 'core/update_movmensalista.html', data)
