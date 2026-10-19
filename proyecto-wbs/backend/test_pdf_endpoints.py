import urllib.request
import json

base = "https://nine524.onrender.com"

# 1. Catálogos
catalogs = [
    "/interests",
    "/interests/1/subinterests",
    "/levels",
    "/languages",
    "/modalities",
    "/durations",
]

print("Probando catálogos en producción...")
for ep in catalogs:
    url = base + ep
    with urllib.request.urlopen(url) as r:
        assert r.getcode() == 200
        data = json.loads(r.read().decode())
        print(f" [200 OK] {ep:30} -> {len(data)} elementos")

# 2. Creación con multipart/form-data
print("\nProbando POST /me/teaching-offers con multipart/form-data...")
boundary = "WebKitFormBoundary7MA4YWxkTrZu0gW"
payload_data = json.dumps({
    "title": "Clases de Álgebra",
    "description": "Refuerzo de álgebra para secundaria...",
    "interest_id": 1,
    "subinterest_id": 2,
    "level_taught": "beginner",
    "language": "es",
    "max_students": 1,
    "modality": "in_person",
    "location": {
        "province": "Buenos Aires",
        "city": "La Plata",
        "zone": "Centro"
    },
    "credits_cost": 2,
    "time_zone": "America/Argentina/Buenos_Aires",
    "availability": [
        {"day": "mon", "start_time": "18:00", "end_time": "19:00"}
    ],
    "duration_minutes": 60
})

body_parts = [
    f"--{boundary}",
    'Content-Disposition: form-data; name="data"',
    "",
    payload_data,
    f"--{boundary}--",
    ""
]
body_bytes = "\r\n".join(body_parts).encode("utf-8")

req = urllib.request.Request(
    base + "/me/teaching-offers",
    data=body_bytes,
    headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    status_code = resp.getcode()
    res = json.loads(resp.read().decode())
    assert status_code == 201
    assert res["status"] == "active"
    assert res["moderation_status"] == "active"
    assert res["duration_minutes"] == 60
    assert res["credits_cost"] == 2
    print(f" [201 CREATED] Oferta creada exitosamente con ID #{res['id']}")
    print(f"               Título: {res['title']}")
    print(f"               Estado: {res['status']} | Moderación: {res['moderation_status']}")

print("\n¡TODAS LAS PRUEBAS EN PRODUCCIÓN PASARON CON ÉXITO!")
