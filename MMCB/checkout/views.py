from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import reduce
from datetime import datetime
from carton.cart import Cart
from checkout.models import PurchaseOrder
from members.models import PersonalInfo
from products.models import Detail


def checkout_page(request):
    errors = []
    cart = Cart(request.session)
    cost_total = cart.total
    if cart.is_empty:
        return redirect(reverse('store'))
    else:
        if request.POST:
            cart_list = [v for k, v in cart.cart_serializable.items()]
            cal_price = reduce(lambda x, y: x + y, [i['quantity'] * int(i['price']) for i in cart_list])
            delivery = request.POST.get('delivery')
            try:
                shopper = PersonalInfo.objects.get(id=request.user.personalinfo.id)
                if cart.total == cal_price and delivery is not None:
                    order = PurchaseOrder.objects.create(
                        number=0,
                        shopper=shopper,
                        order_date=datetime.now(),
                        freight=60 if delivery == '7-11' else 80
                        if delivery == 'postoffice' else 120
                        if delivery == 'homedelivery' else 1000,
                        total=cart.total,
                        notes=request.POST.get('shopper_notes'),
                        order_notes=cart_list
                    )
                    order.number = float(datetime.now().strftime('%y%m%d%H%M%S')) + float(order.id)
                    order.total = order.total + order.freight
                    for d in cart_list:
                        detail_item = get_object_or_404(Detail, id=d['product_pk'])
                        order.sold_goods.add(detail_item)
                        if detail_item.stock - d['quantity'] >= 0:
                            detail_item.stock -= d['quantity']
                        else:
                            return redirect(reverse('cart:shopping-cart-show'))
                        detail_item.sold += d['quantity']
                        detail_item.total_sold += d['quantity']
                        # print ('id={} / 存貨={} / 售貨={} / 總售貨={}'.format(
                        #     detail_item.id, detail_item.stock,
                        #     detail_item.sold, detail_item.total_sold
                        # ))
                        detail_item.save()
                    order.save()
                    cart.clear()
                    return HttpResponseRedirect(reverse('checkout:orderinfo'))
                else:
                    errors.append('資料有誤 或 尚未填寫，請重新整理再次一次')
            except:
                return redirect(reverse('member:info'))
    context = {
        'title': '結帳清單',
        'errors': errors,
        'cost_total': cost_total,
    }
    return render(request, 'checkout/checkout-page.html', context)


def checkout_orderinfo(request):
    errors = []
    newest_order = None
    user_orderlist = request.user.personalinfo.purchaseorder_set.all()
    try:
        newest_orderid = user_orderlist.order_by('-order_date')[0].id
        newest_order = get_object_or_404(PurchaseOrder, id=newest_orderid)
    except:
        errors.append('無法取得訂單資料')
    context = {
        'title': '訂單資訊',
        'myorder': newest_order,
        'errors': errors,
    }
    return render(request, 'checkout/checkout-orderinfo.html', context)
