# Estrategia de Datos de Prueba (Mock Data) y Seeding

**Proyecto:** GDSI 2026 — Plataforma de Intercambio de Aprendizajes  
**Repositorio de implementación backend:** `9524-backend`  
**Repositorio maestro de especificación y WBS:** `95.24` (`proyecto-wbs`)  
**Fecha de definición:** Octubre 2026  

---

## 1. Principio Fundamental de Aislamiento

* **`9524-backend` (Repo del Grupo):** Debe contener **exclusivamente código Python limpio, idiomático y profesional**. Está terminantemente prohibido incluir trazas de IA, prompts, agentes, notas de asistencia o documentación no solicitada por el equipo.
* **`95.24` (Repo Maestro):** Es la fuente de verdad para la arquitectura, especificaciones (SDD), WBS, Jira y directivas de agentes.

---

## 2. Estrategia de Ramas y Datos en `9524-backend`

Para no interferir con el flujo de trabajo de los compañeros de equipo ni romper sus entornos locales:

1. **Ramas principales (`main`, `feature/1.5-busqueda-publicaciones`):**
   * Conservan la base de datos pequeña original (~14 usuarios, publicaciones de prueba básicas).
   * Se inicializan y reinician con el comando estándar del equipo:
     ```bash
     python -m db.manage reset
     ```
   * Todas las pruebas unitarias existentes (`tests/test_database.py`, etc.) corren y pasan al 100% sobre este conjunto base.

2. **Rama dedicada de Mock (`feature/mock-data`):**
   * Contiene el script independiente [`db/seed_mock.py`](file:///c:/dev/9524-backend/db/seed_mock.py).
   * Nace sobre los cambios de la Épica 1.5 (Buscador y compatibilidad), permitiendo al equipo de Frontend contar tanto con la API de búsqueda como con un volumen de datos robusto para probar tarjetas, filtros y paginación.
   * Ejecución en un solo paso:
     ```bash
     python -m db.seed_mock
     ```

---

## 3. Arquitectura del Seeder Ampliado (`seed_mock.py`)

A diferencia de un volcado estático (`dump.sql`), `seed_mock.py` es un script activo de **SQLAlchemy ORM** que aplica lógica de dominio e integridad referencial:

* **Auto-creación de tablas:** Verifica `Base.metadata.create_all(bind=engine)` antes de insertar. Quien clona el repositorio no necesita ejecutar `manage reset` previamente; el script inicializa el archivo `.db` y sus 16 tablas de forma autónoma.
* **Idempotencia:** Si se ejecuta sobre una base existente, actualiza y vincula los registros sin duplicar filas ni lanzar errores de clave primaria/única.
* **Seguridad de codificación en Windows:** Configura `sys.stdout.reconfigure(encoding="utf-8")` y utiliza textos limpios para evitar excepciones por el codec `cp1252` en PowerShell / CMD.

### Catálogo de Entidades Pobladas (16 Tablas, 0 Tablas Vacías)

| Tabla | Registros | Descripción de Dominio |
|---|:---:|---|
| `users` | **40** | Perfiles variados con nombres reales, fotos, biografías, roles (admin, user, suspendido, baneado), modalidades y ubicaciones. |
| `categories` | **9** | Tecnología, Idiomas, Música, Cocina, Cerámica, Bienestar, Negocios, Creatividad, Matemáticas. |
| `skills` | **30** | Habilidades específicas mapeadas a cada categoría de aprendizaje. |
| `badges` | **4** | Primer Paso, Maestro Colaborativo, Perfil Verificado, Miembro Solidario. |
| `prohibited_words` | **11** | Términos restringidos para moderación automática. |
| `offered_skills` | **58** | Ofertas de clases activas con precios en créditos, niveles y duración estimada. |
| `offered_skill_availability` | **64** | Franjas horarias recurrentes por oferta (días de semana, horarios mañana/tarde/noche). |
| `desired_skills` | **54** | Intereses de aprendizaje cargados por los usuarios para alimentar el motor de compatibilidad recíproca. |
| `user_availabilities` | **63** | Franjas horarias personales de los aprendices. |
| `user_badges` | **75** | Insignias otorgadas según el historial de cada miembro. |
| `session_requests` | **23** | Solicitudes y clases en distintos estados (`pending`, `confirmed`, `completed`, `cancelled`, `rejected`). |
| `ratings` | **20** | Reseñas y calificaciones con comentarios realistas y puntajes que alimentan el promedio de reputación. |
| `credit_reservations` | **5** | Reservas temporales asociadas a sesiones pendientes. |
| `credit_transactions` | **56** | Libro mayor contable: créditos de bienvenida (+20), transferencias por clases consumidas y reembolsos. |
| `reports` | **4** | Denuncias de prueba para moderación de contenido. |

---

## 4. Optimización de Imágenes de Portada

* **Problema detectado:** En el seed original, cada publicación subía un archivo binario independiente a Supabase S3 (`publications/seed/{hash}.webp`), provocando 66 subidas de red individuales que demoraban más de un minuto.
* **Solución aplicada:**
  1. Se alojaron las 9 portadas oficiales por categoría en Supabase Storage público bajo la ruta:
     `https://<project-ref>.supabase.co/storage/v1/object/public/gdsi/covers/{categoria}.webp`
  2. `seed_mock.py` asigna directamente la URL correspondiente según el `interest_id` de la publicación.
  3. Tiempo de red para imágenes en seed: **0 segundos**.

---

## 5. Estrategia de Motor: SQLite Local vs. Nube (Supabase)

El backend soporta ambos entornos mediante la configuración de `DATABASE_URL` en el archivo `.env`:

```ini
# Entorno local (Recomendado para desarrollo ágil y Frontend):
DATABASE_URL=sqlite:///./local_dev.db

# Entorno remoto (Supabase / PostgreSQL):
# DATABASE_URL=postgresql+psycopg://postgres.<ref>:<pw>@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require
```

### ¿Por qué SQLite local para el Frontend?
* **Latencia cero:** Al correr sobre disco local/RAM, el seeder completo ejecuta más de 350 operaciones de verificación e inserción en **3 segundos**.
* **Soporte multihilo:** En [`app/db.py`](file:///c:/dev/9524-backend/app/db.py) se configuró `connect_args={"check_same_thread": False}` cuando el engine es SQLite, garantizando concurrencia total con el servidor de desarrollo `fastapi dev`.
* **Sin conflictos de red:** El desarrollador de frontend puede trabajar 100% offline sin depender de la cuota o disponibilidad de Supabase.
* **Protección Git:** `local_dev.db` y `*.sqlite3` se encuentran excluidos en [`.gitignore`](file:///c:/dev/9524-backend/.gitignore).
