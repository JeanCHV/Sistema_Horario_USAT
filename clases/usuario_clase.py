class Usuario:
    id=0
    username=""
    password=""
    idpersona=""
    tipo_usuario   =""

    def __init__(self, u_id, u_username,u_password, u_idpersona, u_id_Estado):
        self.id=u_id
        self.username=u_username
        self.password =u_password
        self.idpersona=u_idpersona
        self.id_estado=u_id_Estado

    def obtenerObjetoSerializable(self):
        dicctemp=dict()
        dicctemp["id"]=self.id
        dicctemp["username"]=self.username
        dicctemp["password"]=self.password
        dicctemp["id_persona"]=self.idpersona
        dicctemp["id_estado"]=self.id_estado
        return dicctemp

    def __str__(self):
        return "User(id='%s')" % self.id