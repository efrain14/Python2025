"""comprobar si un usuario ha sido baneado para hacer las compras"""
usuarios_baneados = ["carlos", "juan", "pedro", "luis"]
usuario = "maria"
if usuario not in usuarios_baneados:
    print(f"{usuario.title()}, tu puedes realizar la compra")
