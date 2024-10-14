from django.shortcuts import render


def platform(request):
    title = "Магазин игр"
    head = "Главная страница"
    context = {
        "title": title,
        "head": head
    }
    return render(request, 'main_page.html', context)


def shop_game(request):
    title = "Страница Игр"
    head = "Игры"
    button = "Купить"
    context = {
        "title": title,
        "head": head,
        "button": button,
    }
    return render(request, 'shop_game.html', context)


def cart_page(request):
    title = "Корзина"
    head = "Корзина"
    context = {
        "title": title,
        "head": head,
    }
    return render(request, 'cart_page.html', context)