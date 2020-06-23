##########################################################
#프로그램명: 배송지 저장
#작성자 : 권동천
#수정일 : 2020-06-21
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 결제가 끝나고 각 정보를 데이터베이스에 저장
##########################################################

def Payment2(request, id):
    product = Product.objects.get(pk=id)
    user = User.objects.all()
    login = Check_user()

    for item in user:
        if item.status == 1:
            user = item
            break

    if request.method == "POST" :
        delivery_location = request.POST.get("delivery_location")
        name = user.name
        recipient = request.POST.get("recipient")
        phone_number = request.POST.get("phone_number")
        payment_method = request.POST.get("payment_method")
        bank_name = request.POST.get("bank_name")
        bank_owner = request.POST.get("bank_owner")
        card_number = request.POST.get("card_number")
        product_name = product.description

    user_info = User_Info(
        name=name, 
        delivery_location=delivery_location, 
        recipient=recipient, 
        phone_number=phone_number,
        payment_method=payment_method,
        bank_name=bank_name,
        bank_owner=bank_owner,
        card_number=card_number,
        product_name=product_name,
    )
    user_info.save()
    return render(request, 'main.html', {'login':login})
