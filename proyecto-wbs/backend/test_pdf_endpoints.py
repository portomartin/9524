import urllib.request
import urllib.error
import json

base = "https://nine524.onrender.com"

# 1. Catálogos
print("1. Probando catálogos en producción...")
catalogs = ["/interests", "/interests/1/subinterests", "/levels", "/languages", "/modalities", "/durations"]
for ep in catalogs:
    url = base + ep
    with urllib.request.urlopen(url) as r:
        assert r.getcode() == 200
        data = json.loads(r.read().decode())
        print(f"   [200 OK] {ep:32} -> {len(data)} elementos")

# Test 404 en subinterés inexistente (Página 10 del PDF)
try:
    urllib.request.urlopen(base + "/interests/999/subinterests")
    print("   [FALLO] Debería haber dado 404 en interés 999")
except urllib.error.HTTPError as e:
    assert e.code == 404
    print("   [404 NOT FOUND] /interests/999/subinterests verificado con éxito")

def post_offer(payload_dict):
    boundary = "WebKitBoundary123"
    body_parts = [
        f"--{boundary}",
        'Content-Disposition: form-data; name="data"',
        "",
        json.dumps(payload_dict),
        f"--{boundary}--",
        ""
    ]
    data = "\r\n".join(body_parts).encode("utf-8")
    req = urllib.request.Request(
        base + "/me/teaching-offers",
        data=data,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST"
    )
    return req

# 2. Test Happy Path (201 Created)
print("\n2. Probando Happy Path (POST /me/teaching-offers)...")
valid_payload = {
    "title": "Clases de Álgebra",
    "description": "Refuerzo de álgebra para secundaria...",
    "interest_id": 1,
    "subinterest_id": 1,
    "level_taught": "beginner",
    "language": "es",
    "max_students": 1,
    "modality": "in_person",
    "location": {"province": "Buenos Aires", "city": "La Plata", "zone": "Centro"},
    "credits_cost": 2,
    "time_zone": "America/Argentina/Buenos_Aires",
    "availability": [{"day": "mon", "start_time": "18:00", "end_time": "19:00"}],
    "duration_minutes": 60
}
with urllib.request.urlopen(post_offer(valid_payload)) as resp:
    assert resp.getcode() == 201
    res = json.loads(resp.read().decode())
    assert res["status"] == "active"
    print(f"   [201 CREATED] Oferta creada exitosamente ID #{res['id']} con status: {res['status']}")

# 3. Test Mini Rules de Validación (422 Unprocessable Entity)
print("\n3. Probando Mini-Rules de Validación (422)...")

# A. Título vacío
bad_title = dict(valid_payload)
bad_title["title"] = "   "
try:
    urllib.request.urlopen(post_offer(bad_title))
    print("   [FALLO] Debería haber dado 422")
except urllib.error.HTTPError as e:
    assert e.code == 422
    err_body = json.loads(e.read().decode())
    assert "title" in err_body["detail"]["errors"]
    print(f"   [422 OK] Validación 'title': {err_body['detail']['errors']['title']}")

# B. Modality online pero enviando location (CA3 del PDF)
bad_location = dict(valid_payload)
bad_location["modality"] = "online"
bad_location["location"] = {"city": "La Plata"}
try:
    urllib.request.urlopen(post_offer(bad_location))
    print("   [FALLO] Debería haber dado 422")
except urllib.error.HTTPError as e:
    assert e.code == 422
    err_body = json.loads(e.read().decode())
    assert "location" in err_body["detail"]["errors"]
    print(f"   [422 OK] Validación 'location en online': {err_body['detail']['errors']['location']}")

# C. Horario start_time >= end_time (CA4 del PDF)
bad_hours = dict(valid_payload)
bad_hours["availability"] = [{"day": "mon", "start_time": "19:00", "end_time": "18:00"}]
try:
    urllib.request.urlopen(post_offer(bad_hours))
    print("   [FALLO] Debería haber dado 422")
except urllib.error.HTTPError as e:
    assert e.code == 422
    err_body = json.loads(e.read().decode())
    assert "availability.0.end_time" in err_body["detail"]["errors"]
    print(f"   [422 OK] Validación 'availability.0.end_time': {err_body['detail']['errors']['availability.0.end_time']}")

print("\n¡TODAS LAS VALIDACIONES Y COMPORTAMIENTOS DEL PDF VERIFICADOS CON ÉXITO!")
