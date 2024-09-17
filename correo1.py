import smtplib
from dotenv import load_dotenv
import os 
load_dotenv()
try:
    #debes de crear un archivo .env y hacer las  variables de entorno con tus propias credenciales
    remitente = os.getenv('remitente')
    destinatario = os.getenv('destinatario')
    serv = "smtp.gmail.com"
    puerto = 587
    contrasena = os.getenv('contrasena')
    conex = smtplib.SMTP(serv,puerto)
    conex.starttls()
    conex.login(remitente,contrasena)
    conex.sendmail(remitente,destinatario,"Subject: Probando correo" + "\n\n Este correo es automatico usando la libreria smtplib")
    print("El correo se ha mandado correctamente")
except smtplib.SMTPException as e:
    print(f"Error al mandar el mensaje: {e}")
finally:
    conex.quit()