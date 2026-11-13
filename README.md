# MAILTRACE AI

> Pre-open email threat detection, explainable security intelligence, and digital forensics.

MAILTRACE AI is an email-security project that combines Gmail integration, pre-open threat scanning, email-authentication analysis, machine-learning/NLP signals, threat-intelligence enrichment, campaign correlation, and case-based investigation.

## Repository status

This repository is being upgraded from an archive-only starting point. The complete application source, setup instructions, test guidance, security documentation, and contributor workflows are being added in the `chore/production-ready-repository` branch. Review the pull request before merging.

## Key project areas

- `backend/` — FastAPI application, Gmail integration, persistence, services, and automated tests.
- `frontend/` — React Native / Expo client for web and mobile.
- `forensics/` — Email parsing, header analysis, and authentication checks.
- `intelligence/` — DNS, RDAP, reputation, and approximate IP geolocation enrichment.
- `graph/` — Campaign correlation and incident timelines.
- `ml/` — Model inference code and checkpoint location.
- `docs/` — Architecture, feature, and demonstration guides.

## Quickstart

See the complete setup guide in the upgrade branch's README. In brief:

```bash
git clone https://github.com/hrsubhut/MAILTRACE.git
cd MAILTRACE
python -m venv .venv
# Activate the virtual environment, then:
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload
```

In a second terminal:

```bash
cd frontend
npm ci
npm run web
```

## Important model note

The uploaded project archive did not contain the real trained `model.safetensors` checkpoint; it contained a 134-byte placeholder although its manifest describes a 267,832,560-byte file. Do not treat transformer inference as active until the authentic weights are obtained from an approved source and their SHA-256 is verified against the model manifest. The application includes fallback behavior when weights are unavailable.

## Security

Do not commit `.env` files, Google OAuth credentials, tokens, private mailbox exports, `.eml`/`.msg` files, logs containing personal data, or production database dumps. Keep Gmail actions user-confirmed. Treat all threat scores and enrichment as decision support, not definitive attribution.

## License

Apache-2.0. See `LICENSE` in the full source tree.
