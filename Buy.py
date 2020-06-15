########################################################
#프로그램명: 결제, 재고관리 기능
#작성자 : 권동천
#수정일 : 2020-06-12
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 결제할 상품의 상태에 따라 결제를 진행
########################################################
from django.shortcuts import render
from products.models import Product
from users.models import User

def Buy(request, id):
    product = Product.objects.get(pk=id)
    login = Check_user()

    return render(request, 'Buy.html', {'product' : product, 'login':login})
    
def Buy2(request, id):
    product = Product.objects.get(pk=id)
    buy_num = request.GET.get("buy_num")
    login = Check_user()

    if login == 0 :
        error = int(4)
        return render(request, 'Buy.html', {'product' : product, 'status' : error, 'login':login})
    if product.item_num <= 0 :
        error = int(2)
        return render(request, 'Buy.html', {'product' : product, 'status' : error, 'login':login})
    if (product.item_num - int(buy_num)) < 0 :
        error = int(1)
        return render(request, 'Buy.html', {'product' : product, 'status' : error, 'login':login})
    if int(buy_num) < 0 :
        error = int(3)
        return render(request, 'Buy.html', {'product' : product, 'status' : error, 'login':login})
    product.item_num = product.item_num - int(buy_num)
    product.save()

    preplace=product.price.replace(",","")
    preplace=preplace.replace("원","")
    price = int(buy_num) * int(preplace)
    return render(request, 'Buy2.html', {'product' : product, 'login':login, 'buy_num':buy_num, 'price':price})
