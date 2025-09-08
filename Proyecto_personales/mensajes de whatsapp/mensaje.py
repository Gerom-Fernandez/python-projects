import pywhatkit as kit

# Número de destino con código de país
# Ejemplo Chile: +56 (código país) + 9 (celular) + número
numero = "+56999720338"

# Mensaje a enviar
mensaje = "Hola 👋, este es un mensaje automático con pywhatkit 🚀"

# Enviar mensaje de inmediato
# wait_time = segundos que espera antes de mandar (puedes bajarlo si tu internet es rápido)
# tab_close = True para que cierre la pestaña después de enviar
kit.sendwhatmsg_instantly(numero, mensaje, wait_time=10, tab_close=True)

print("✅ Mensaje enviado con éxito")
