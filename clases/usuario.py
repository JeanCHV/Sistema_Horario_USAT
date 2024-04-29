class Usuario:
    idusuario = 0
    username = ""
    password = ""
    estado = True
    idpersona = 0
    token = ""

    def __init__(self, p_idusuario,p_username,p_password,p_estado,p_idpersona,p_token):
        self.idusuario = p_idusuario
        self.username = p_username
        self.password = p_password
        self.estado = p_estado
        self.idpersona = p_idpersona
        self.token = p_token

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["idusuario"] = self.idusuario
        dict_temp["username"] = self.username
        dict_temp["password"] = self.password
        dict_temp["estado"] = self.estado
        dict_temp["idpersona"] = self.idpersona
        dict_temp["token"] = self.token

        return dict_temp
