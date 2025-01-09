from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Agendamento
from datetime import datetime

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        mensagem = request.POST.get('mensagem')

        # Verificar se já existe agendamento para esta data e horário
        if Agendamento.objects.filter(data=data, horario=horario).exists():
            messages.error(request, 'Este horário já está agendado. Por favor, escolha outro horário.')
            return redirect('home')

        # Criar novo agendamento
        Agendamento.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            data=data,
            horario=horario,
            mensagem=mensagem
        )
        messages.success(request, 'Consulta agendada com sucesso! Entraremos em contato para confirmar.')
        return redirect('home')

    return render(request, 'core/home.html', {
        'horarios': Agendamento.HORARIOS_CHOICES
    })
