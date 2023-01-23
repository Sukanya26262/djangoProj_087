from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def showMyData(request):
    studentid = "65342310087-6"
    fullname = "สุกัลญา ชินคำ"
    nickname = "อ้อน"
    age = 21
    cardid = "1419902021055"
    gender = "หญิง"
    favorite = "ตุ๊กตาหมี"
    career = "นักเรียน"
    favoritefood = "ส้มตำ"
    Dislikedfood = "ต้มเครื่องใน"
    products = []
    product = ['Neo', 2350.00, 'images/neo.jpg ']
    products.append(product)
    product = ['Stan Smith Lux', 5800.00, 'images/2.jpg ']
    products.append(product)
    product = ['Forum Low', 4000.00, 'images/3.jpg ']
    products.append(product)
    product = ['Run Falcon', 1320.00, 'images/4.jpg ']
    products.append(product)
    product = ['Air Force 1', 3700.00, 'images/5.jpg ']
    products.append(product)
    product = ['Air Max', 5300.00, 'images/6.jpg ']
    products.append(product)
    product = ['Retro GTS', 2100.00, 'images/7.jpg ']
    products.append(product)
    product = ['Free Run', 3500.00, 'images/8.jpg ']
    products.append(product)
    product = ['Chuck Taylo All Star', 2700.00, 'images/9.jpg ']
    products.append(product)
    product = ['Point Star', 1500.00, 'images/10.jpg ']
    products.append(product)
    context = {'studentid': studentid, 'fullname': fullname, 'nickname': nickname, 'age': age, 'cardid': cardid,
               'gender': gender, 'favorite': favorite, 'career': career, 'favoritefood': favoritefood,
               'Dislikedfood': Dislikedfood, 'products': products}
    return render(request, 'showMyData.html', context)

productList = []
def showProduct(request):
    product = showProduct[request]
    product = showProduct['P0001','Mouse','Aser',500.00,120]
    productList.append(product)
    product = showProduct['P0002', 'Keyboard', 'Aser', 500.00, 120]
    productList.append(product)
    product = showProduct['P0003', 'Notbook', 'Aser', 500.00, 120]
    productList.append(product)
    product = showProduct['P0004', 'Personal', 'Aser', 500.00, 120]
    productList.append(product)
    product = showProduct['P0005', 'Scanner', 'Aser', 500.00, 120]
    productList.append(product)
    context = {'product':productList}
    return render(request,'showowerProduct.html',context)
