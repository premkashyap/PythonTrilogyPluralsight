class shipping_container:
    serial_number = 1337
    category = 'U'
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial_number = shipping_container.serial_number
        shipping_container.serial_number +=1
        # self.serial_number = self.serial_number +2
        # self.serial_number = self.serial_number #same effect but confusing.
        # self.serial_number +=1

class shipping_container_with_static_method:
    serial_number = 1337


    @staticmethod
    def _get_next_serial():
        result = shipping_container_with_static_method.serial_number
        shipping_container_with_static_method.serial_number+=1
        return result

      

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial_number = shipping_container_with_static_method.serial_number
        shipping_container_with_static_method.serial_number +=1

class shipping_container_with_class_method:
    serial_number = 1337
    HEIGHT_FT = 8.0
    WIDTH_FT =8.0
    FRIDGE_VOLUME_FT3 = 100


    @classmethod
    def _get_next_serial(cls):
        result = cls.serial_number
        cls.serial_number+=1
        return result

    @classmethod #using @classmethod to create multiple constructors
    def empty_container(cls, owner_code, length_ft ,*args, **kwargs):
        return cls(owner_code, length_ft, contents=None,  *args, **kwargs)
    
    @classmethod
    def container_with_items(cls, owner_code, length_ft, items,*args, **kwargs):
        return cls(owner_code, length_ft, list(items),*args, **kwargs)
        
    @property
    def volume_ft3(self):
        return shipping_container_with_class_method.HEIGHT_FT*shipping_container_with_class_method.WIDTH_FT*self.length_ft
        

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.serial_number = shipping_container_with_class_method.serial_number
        shipping_container_with_class_method.serial_number +=1

class RefrigeratedShippingContainer(shipping_container_with_class_method):
    MAX_CELSIUS = 4.0
    
    @staticmethod
    def _c_to_f(celsius):
        return celsius*9/5 + 32
    
    @staticmethod
    def _f_to_c(farenheit):
        return (farenheit-32)*5/9
    
    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value>RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value
    
    @property
    def farenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)
    
    @farenheit.setter
    def farenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return super().volume_ft3-self.FRIDGE_VOLUME_FT3

class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20.0

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS
                <= value
                <= HeatedRefrigeratedShippingContainer.MAX_CELSIUS):
            raise ValueError("Temperatur out of range!")
        self._celsius=value
     

cont = HeatedRefrigeratedShippingContainer("PREM", 10, "Sabji", 2)
print(cont.owner_code)
print(cont.contents)
print(cont.serial_number)
print(shipping_container_with_class_method.serial_number)
print(cont.volume_ft3)