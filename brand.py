class Brand:
    def __init__(self, name, price, salePrice, kg, offer=False):
        self.name = name
        self.price = price
        self.salePrice = salePrice
        self.kg = kg
        self.offer = offer

    def get_KG_price(self, priceMode):
        price_mode = self.setPriceMode(priceMode)
        return price_mode / self.kg

    def get_HALFKG_price(self, priceMode):
        return self.get_KG_price(priceMode) / 2

    def get_QUARTERKG_price(self, priceMode):
        return self.get_HALFKG_price(priceMode) / 2

    def setPriceMode(self, priceMode):
        if priceMode == "purchasePrice":
            return self.price
        elif priceMode == "salePrice":
            return self.salePrice

    def get_ANYKG_price(self, grams: float, priceMode="salePrice") -> float:
        """This function calculates and return the sale price of given grams

        Args:
            grams (float): grams

        Returns:
            float: sale price
        """
        price_mode = self.setPriceMode(priceMode)
        # discount is ???
            #INCOMPLETE.
        if self.offer == True and grams >= 10000:
            return price_mode / (self.kg / (grams / 1000))
        else:
            return price_mode / (self.kg / (grams / 1000))

    def __str__(self):
        if self.offer == True:
            offer = "Si"
        else:
            offer = "No"
        return f"Nombre: {self.name}, Precio de compra: {self.price}, Precio de venta: {self.salePrice}, KGs: {self.kg}, Oferta: {offer}"