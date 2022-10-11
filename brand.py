class Brand:
    def __init__(self, name, price, salePrice, kg, offer=False):
        self.name = name
        self.price = price
        self.salePrice = salePrice
        self.kg = kg
        self.offer = offer

    def get_KG_price(self, priceType):
        price_type = self.setPriceMode(priceType)
        return price_type / self.kg

    def get_ANYKG_price(self, grams: float, priceType="salePrice") -> float:
        """This function calculates and return the sale price of given grams

        Args:
            grams (float): grams
            priceType (string): price type = salePrice or costPrice
        Returns:
            float: sale price
        """
        price_mode = self.setPriceType(priceType)
        # discount is ???
            #INCOMPLETE.
        if self.offer == True and grams >= 10000:
            return price_mode / (self.kg / (grams / 1000))
        else:
            return price_mode / (self.kg / (grams / 1000))

    def setPriceType(self, priceType):
        if priceType == "costPrice":
            return self.price
        elif priceType == "salePrice":
            return self.salePrice

    def __str__(self):
        if self.offer == True:
            offer = "Si"
        else:
            offer = "No"
        return f"Nombre: {self.name}, Precio de compra: {self.price}, Precio de venta: {self.salePrice}, KGs: {self.kg}, Oferta: {offer}"