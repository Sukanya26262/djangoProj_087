from django.db import models


class Product:
    def __init__(self, model, brand, ram, ssd, cpu, price):
        self.model = model
        self.brand = brand
        self.ram = ram
        self.ssd = ssd
        self.cpu = cpu
        self.price = price

    def getNet(self):
        net = float(self.price) - float(self.getDiscount()) + self.getVat()
        return net

    def getVat(self):
        vat = float(self.price) * 0.07
        return vat

    def getDiscount(self):
        discount = float(self.price) * 0.05
        return discount

    def __str__(self):
        return "model: {},brand: {},ram: {},ssd: {},cpu: {},price: {}" \
            .format(self.model, self.brand, self.ram, self.ssd, self.cpu, self.price)
