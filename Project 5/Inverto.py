class InversorString:
    def __init__(self, texto):
        self.texto = texto

    def inverter(self):
        texto_invertido = ""
        for caractere in self.texto:
            texto_invertido = caractere + texto_invertido
        return texto_invertido

texto = "Calde de cana"
inversor = InversorString(texto)
texto_invertido = inversor.inverter()
print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")

texto_usuario = input("Digite uma string para inverter: ")
inversor_usuario = InversorString(texto_usuario)
texto_invertido_usuario = inversor_usuario.inverter()
print(f"Texto original: {texto_usuario}")
print(f"Texto invertido: {texto_invertido_usuario}")
