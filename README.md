# Landing Page - Dra. Giovanna Cecília

Landing page profissional desenvolvida para a Dra. Giovanna Cecília, especialista em Harmonização Facial e procedimentos estéticos.

## Tecnologias Utilizadas

- Django
- Bootstrap
- Font Awesome
- HTML/CSS
- JavaScript

## Funcionalidades

- Apresentação profissional
- Galeria de resultados (antes/depois)
- Seção de serviços
- Formulário de agendamento
- Integração com Instagram
- Design responsivo

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/GIOVANNA-CECILIA.git
cd GIOVANNA-CECILIA
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

6. Acesse http://localhost:8000 no seu navegador

## Estrutura do Projeto

```
GIOVANNA-CECILIA/
├── core/                   # Aplicação principal
│   ├── templates/         # Templates HTML
│   ├── static/           # Arquivos estáticos
│   └── ...
├── static/                # Arquivos estáticos globais
├── manage.py             # Script de gerenciamento Django
└── requirements.txt      # Dependências do projeto
```

## Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
