Retro Arcade ShooterTrabajo Práctico Integrador — Programación IIUn videojuego arcade de naves 2D en Python con arquitectura orientada a objetos, patrones de diseño GoF y persistencia relacional.📋 Resumen del ProyectoRetro Arcade Shooter es una aplicación interactiva desarrollada sobre Pygame que combina mecánicas de disparo tradicionales en 2D con una arquitectura de software desacoplada y escalable.El sistema implementa persistencia de datos mediante MySQL para la gestión de usuarios, puntuaciones máximas e historial de partidas, garantizando una separación clara entre las capas de dominio, presentación y acceso a datos.👥 Equipo de DesarrolloNombre y ApellidoRol / ContribuciónPriscila ToledanoDesarrollo de Software & ArquitecturaTomas NavedaDesarrollo de Software & ArquitecturaClaudio PerezDesarrollo de Software & ArquitecturaSelene QuinteroDesarrollo de Software & Arquitectura🌌 Contexto y NarrativaEn un escenario futurista, la galaxia enfrenta la incursión masiva de flotas hostiles compuestas por tres facciones alienígenas (Abejitas, Platillos y Tanques Mecánicos). El jugador asume el control de una nave estelar de combate con la misión de defender el espacio profundo, sobrevivir a oleadas incrementales de enemigos y registrar su rendimiento en el sistema central.📐 Patrones de Diseño ImplementadosLa arquitectura del proyecto aplica rigurosamente 7 patrones de diseño de la pandilla de los cuatro (GoF) para favorecer la mantenibilidad y la cohesión del código:PatrónClases / MódulosRol Arquitectónico y ResponsabilidadSingletonDatabaseConnectionSoundManagerAsegura una única instancia compartida para la conexión a MySQL y el motor de audio, evitando redundancia de conexiones y uso ineficiente de memoria.Factory MethodEnemyFactoryBulletFactoryEncapsula la lógica de instanciación de entidades (enemigos y proyectiles), permitiendo añadir nuevos tipos de objetos sin alterar el código cliente.ObserverGameStats (Subject)HUD (Observer)Emite eventos reactivos ante cambios en el puntaje, vidas o nivel actual, actualizando la interfaz gráfica de forma desacoplada.StateStateManagerLoginState, MenuStatePlayingState, PausedStateGameOverStateModela el ciclo de vida de la aplicación mediante máquinas de estado finito, controlando la transición fluida entre pantallas.StrategySimpleMovementZigzagMovementDefine una familia de algoritmos de desplazamiento e interrumpe el acoplamiento rígido de comportamientos en las unidades enemigas.CommandMoveLeftCommandMoveRightCommandShootCommandEncapsula las entradas de control e interacción del jugador en objetos comando ejecutables.DecoratorPlayerDecoratorDoubleShotDecoratorExtiende las funcionalidades de la nave del jugador dinámicamente en tiempo de ejecución (ej. disparos dobles/mejorados) sin recurrir a herencia múltiple.🗄️ Esquema y Persistencia de Datos (MySQL)El sistema utiliza la base de datos relacional juego_prog2 administrada mediante MySQL Workbench:
┌─────────────────────────┐         ┌─────────────────────────┐
│        usuarios         │         │   historial_partidas    │
├─────────────────────────┤         ├─────────────────────────┤
│ id (PK)                 │1       *│ id (PK)                 │
│ username (UNIQUE)       ├─────────┤ user_id (FK)            │
│ current_level           │         │ score                   │
│ max_score               │         │ level_reached           │
└─────────────────────────┘         │ played_at               │
                                    └─────────────────────────┘
usuarios: Registra las credenciales y el estado persistente del jugador (current_level, max_score), facilitando la recuperación automática del progreso al autenticarse.historial_partidas: Guarda una auditoría cronológica de partidas finalizadas con el puntaje obtenido, nivel alcanzado y marca de tiempo (played_at).🛠️ Tecnologías y RequisitosLenguaje: Python 3.10 o superiorMotor Gráfico: Pygame / Pygame Community Edition (pygame-ce)Gestor de BD: MySQL Server 8.0+ / XAMPPLibrerías Clave: mysql-connector-python, python-dotenv⚙️ Instalación y ConfiguraciónClonar el repositorio:Bashgit clone https://github.com/usuario/Juego.prog.git
cd Juego.prog
Crear e inicializar el entorno virtual:PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
Instalar dependencias del sistema:PowerShellpip install -r requirements.txt
Variables de Entorno (.env):Crea un archivo .env en la raíz del proyecto con la configuración de tu motor MySQL:Fragmento de códigoDB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=juego_prog2
DB_PORT=3306
🚀 Modo de UsoAsegurate de iniciar el servicio MySQL y ejecuta el punto de entrada principal:PowerShellpython main.py
🎮 Mapa de Controles      [ W / ↑ ]               [ Space ]                [ Esc ]
      Navegar                 Disparar                  Pausa
         │                        │                       │
 [ A / ← ] [ S / ↓ ] [ D / → ]    │                 [ R ]   /   [ M ]
  Mover Izq. / Mover Der.         │               Reiniciar / Menú Principal
AcciónMapeo TecladoDesplazamiento LateralFlechas Izquierda / Derecha o Teclas A / DAcción de DisparoBarra EspaciadoraControl de MenúFlechas Arriba / Abajo o Teclas W / SConfirmaciónTecla EnterGestión de PausaTecla EscPantalla Game OverTecla R (Reintentar) / Tecla M (Volver al Menú)
