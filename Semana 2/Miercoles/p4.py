email_usuario = "  Contacto@Python.org  "
email_db = "contacto@python.org"

# Intentamos limpiar el string
email_usuario = email_usuario.strip()
email_usuario = email_usuario.lower()

print(f"Comparando: '{email_usuario}' con '{email_db}'")

if email_usuario == email_db:
    print("Acceso concedido.")
else:
    print("Error: El email no coincide.")