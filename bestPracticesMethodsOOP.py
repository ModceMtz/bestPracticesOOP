class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        # Atributos privados
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__no_control = no_control
        self.__semestre = semestre

    # Métodos para establecer los valores de los atributos (Setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores de los atributos (Getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre


# Ejemplo de uso:
alumno = Alumno("Juan", "Pérez", "López", "12345678", 3)

# Obtener valores
print("Nombre:", alumno.get_nombre())
print("Apellido paterno:", alumno.get_apellido_paterno())
print("Apellido materno:", alumno.get_apellido_materno())
print("No. control:", alumno.get_no_control())
print("Semestre:", alumno.get_semestre())

# Modificar valores
alumno.set_nombre("Carlos")
alumno.set_apellido_paterno("Ramírez")
alumno.set_semestre(4)

# Obtener los valores actualizados
print("\nValores actualizados:")
print("Nombre:", alumno.get_nombre())
print("Apellido paterno:", alumno.get_apellido_paterno())
print("Semestre:", alumno.get_semestre())
