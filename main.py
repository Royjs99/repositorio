from clases.clases import *
from repository.repository import *

estudiante = Estudiante("2203042588", "Martinez Nuñez Rodrigo Timoteo")
credencialEstudiante = Credencial(1, estudiante, "firma", "fotografia", "observacion")
solicitarCredencial = CredencialRepository()
solicitarCredencial.solicitudCredencial(estudiante, credencialEstudiante)
print(solicitarCredencial.consultarSolicitudes())
