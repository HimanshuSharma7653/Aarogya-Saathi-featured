"""wger exercise API client with a reliable local fallback."""
import json
import urllib.parse
import urllib.request
import urllib.error

WGER_URL = "https://wger.de/api/v2/exerciseinfo/"


def search_wger_exercises(query="", limit=12):
    """Return normalized wger exercises. Returns [] when the API is unavailable."""
    params = {"limit": max(1, min(int(limit), 30)), "language": 2, "status": 2}
    if query:
        params["search"] = query[:80]
    url = WGER_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "AarogyaSaathi/1.0 (student wellness project)"})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            payload = json.loads(response.read().decode("utf-8"))
        items = []
        for item in payload.get("results", []):
            translations = item.get("translations") or []
            english = next((x for x in translations if x.get("language") == 2), translations[0] if translations else {})
            name = (english.get("name") or "").strip()
            if not name:
                continue
            images = item.get("images") or []
            image = images[0].get("image") if images else None
            items.append({
                "id": item.get("id"), "name": name,
                "description": english.get("description", "") or "Follow the demonstrated movement with controlled form.",
                "image": image, "source": "wger"
            })
        return items
    except (OSError, ValueError, urllib.error.URLError, TimeoutError):
        return []
