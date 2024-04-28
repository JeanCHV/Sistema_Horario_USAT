class Persona:
    idpersona = 0
    nombres = ""
    apellidos = ""
    n_documento = ""
    telefono = ""
    correo = ""
    tipopersona = ""
    cantHoras = 0
    tiempo_ref = 0
    foto = ""

    def __init__(self, p_idpersona,p_nombres,p_apellidos,p_n_documento,p_telefono,p_correo,p_tipopersona,p_cantHoras,p_tiempo_ref,p_foto):
        self.idpersona = p_idpersona
        self.nombres = p_nombres
        self.apellidos = p_apellidos
        self.n_documento = p_n_documento
        self.telefono = p_telefono
        self.correo = p_correo
        self.tipopersona = p_tipopersona
        self.cantHoras = p_cantHoras
        self.tiempo_ref = p_tiempo_ref
        self.foto = p_foto

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["idpersona"] = self.idpersona
        dict_temp["nombres"] = self.nombres
        dict_temp["apellidos"] = self.apellidos
        dict_temp["n_documento"] = self.n_documento
        dict_temp["telefono"] = self.telefono
        dict_temp["correo"] = self.correo
        dict_temp["tipopersona"] = self.tipopersona
        dict_temp["cantHoras"] = self.cantHoras
        dict_temp["tiempo_ref"] = self.tiempo_ref
        dict_temp["foto"] = self.foto

        return dict_temp
