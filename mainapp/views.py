from django.shortcuts import render

def index(request):
    context = {
        'tittle': "GeekShop",
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'tittle': "GeekShop",
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'img': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб. руб.',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'img': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.',
             'description': 'Плотная ткань. Легкий материал.',
             'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.',
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        ]
    }
    return render(request, 'mainapp/products.html', context)
