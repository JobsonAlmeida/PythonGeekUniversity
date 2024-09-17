def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, "#")


print(cabecalho("geek university"))

print(cabecalho("geek university", "geek"))

cabecalho(texto="abc")

texto: str

texto2 : str

