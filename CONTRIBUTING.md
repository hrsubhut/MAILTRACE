# Contributing to MAILTRACE AI

Thank you for helping improve MAILTRACE. Because the project processes mailbox and forensic data, privacy and safe defaults are part of every contribution.

## Development setup

1. Read the root README and the relevant guides under `docs/`.
2. Use Python 3.11+ and create an isolated virtual environment.
3. Install `backend/requirements.txt` and `backend/requirements-dev.txt`.
4. Copy `.env.example` to `.env` and use mock/test credentials.
5. Run `npm ci` from `frontend/`.

## Before opening a pull request

- Run `python -m pytest backend/tests -q` (or document any unavailable optional model dependencies).
- Run `npx tsc --noEmit` from `frontend/`.
- Add tests for behavior changes and update documentation.
- Keep changes focused and explain security implications.
- Never add real email files, mailbox exports, OAuth tokens, API keys, private screenshots, or raw forensic evidence.
- Do not describe model-backed behavior as active unless the authentic model checkpoint is present and verified.

## Pull request checklist

- [ ] The problem and scope are clear.
- [ ] Tests cover changed behavior.
- [ ] Documentation and configuration examples are updated.
- [ ] No secrets or personal mailbox data are included.
- [ ] Security-sensitive actions remain explicit and user-confirmed.
- [ ] Limitations and operational assumptions are documented.
