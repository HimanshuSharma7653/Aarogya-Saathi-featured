# AarogyaSaathi — Exercise Studio Upgrade

## Run on Windows
1. Extract the ZIP.
2. Open the `AarogyaSaathi` folder in VS Code or File Explorer.
3. Double-click `run_windows.bat`, or run `py -3.11 run.py` in PowerShell.
4. Open http://127.0.0.1:5000.
5. Open Exercise from the app navigation.

The launcher creates `.venv`, installs Flask, initializes a fresh local SQLite database and creates a persistent random development secret in `instance/secret_key`. Run `run.py`, not `app.py` directly.

## Exercise Studio features
- Existing built-in exercise suggestions remain available offline.
- Search route `/api/exercises?q=...` queries the public wger exercise catalogue and returns a safe empty result if the external service is unavailable.
- Yoga library includes Mountain, Tree, Cobra, Child's Pose, Seated Forward Bend, Corpse, Warrior I, Warrior II, Bridge and Cat-Cow.
- Supplied yoga guide and six-pose collage are stored locally in `static/images/yoga/`.
- Live camera page uses MediaPipe Pose in the browser. Camera frames are processed client-side and are not sent to the Flask server.

## Live pose detection requirements
- Allow camera permission in the browser.
- Use `http://127.0.0.1:5000` or HTTPS; browsers restrict camera access on insecure remote origins.
- Internet is required to load MediaPipe scripts and model assets from jsDelivr CDN.
- Ensure good lighting and keep the body in the camera frame.
- Warrior II has a basic arm-alignment cue; other poses currently show landmark visibility and general coaching guidance. This is not a clinically validated posture assessment, and it does not diagnose injury or replace a yoga instructor.

## wger API
The server queries the public wger exercise-info endpoint with a short timeout. No API key is required for this basic read-only catalogue query. If wger is down, the built-in exercises continue to display.

## Privacy and safety
Camera frames remain in the browser. Do not use this demo for medical decisions. Stop if you feel pain, dizziness or discomfort. The project still needs a separate full security hardening pass (authentication, ownership checks, CSRF, upload validation, production secret management and HTTPS) before deployment with real personal/health data. Do not expose Flask's development server directly to the public internet.
