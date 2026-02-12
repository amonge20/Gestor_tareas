# Gestor_tareas

# RESUMEN DE LA APP

Gestor de Tareas / Incidencias es una aplicación web construida con Django para gestionar tareas o incidencias en un entorno multiusuario. Permite a los clientes registrar incidencias, a los administradores asignarlas a trabajadores y a los trabajadores gestionar y completar las incidencias asignadas.

# CARACTERISTICAS

- Autenticación de usuarios (login/logout)
- Roles de usuario: Cliente, Administrador, Trabajador
- CRUD de tareas/incidencias: crear, editar, eliminar y ver lista
- Tarjetas estilo Trello para visualizar tareas según estado
- Colores de estado: Pendiente (amarillo), En progreso (azul), Completada (verde)
- Formularios estilizados con Bootstrap y CSS personalizado
- Redirecciones después de login/logout

# TECNOLOGIAS USADAS

- Backend: Python 3.8.2 + Django 4.2.28
- Frontend: HTML, CSS y Bootstrap 5
- Base de datos: SQLite (por defecto, fácilmente migrable a PostgreSQL)
- Estilos: CSS personalizado (`estilo.css`)
- Despliegue: Local, servidor web o Docker (opcional)

# PRÓXIMAS MEJORAS
- Desplegarlo en servidor y acceder desde web o móvil
- API REST para app móvil con Django REST Framework
- Notificaciones por email o WebSocket
- Drag & Drop de incidencias estilo Kanban
- Dashboard con métricas y gráficos