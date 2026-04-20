from django.http import JsonResponse

def product_list(request):
    products = [
        {"name": "Laptop", "price": 55000, "category": "Electronics"},
        {"name": "Phone", "price": 20000, "category": "Electronics"},
        {"name": "Shoes", "price": 1500, "category": "Fashion"},
        {"name": "Watch", "price": 3000, "category": "Accessories"},
    ]
    return JsonResponse(products, safe=False)