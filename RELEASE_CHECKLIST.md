# 🚀 Release-Checkliste für Kerbl SmartCoop Integration

Damit Updates in HACS funktionieren, musst du bei jeder Änderung ein neues Release erstellen.

---

## 1. Versionsnummer anpassen
In `custom_components/kerbl_smartcoop/manifest.json` die Version hochzählen:

```json
"version": "0.0.2"
```

---

## 2. Änderungen committen & pushen
```bash
git add .
git commit -m "Beschreibung der Änderungen"
git push origin main
```

---

## 3. Neuen Tag erstellen
Tag muss der Versionsnummer entsprechen, z. B.:
```bash
git tag -a v0.0.2 -m "Neue Version 0.0.2"
git push origin v0.0.2
```

---

## 4. Release auf GitHub veröffentlichen
1. Auf GitHub → Tab **Releases** öffnen
2. **"Draft a new release"** anklicken
3. Den neuen Tag (`v0.0.2`) auswählen
4. Titel & Beschreibung angeben
5. **Publish release** klicken

---

## ✅ Fertig!
HACS erkennt nun das neue Release und bietet das Update in Home Assistant an.
