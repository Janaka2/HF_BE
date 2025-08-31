# HF Space + GitHub Actions (Secrets-injected)

Minimal template showing how to:
- Keep API keys **in GitHub Secrets** (not in repo).
- Auto-deploy to a **Hugging Face Space** on push to `main`.
- Inject secrets into the Space via API so the backend reads them from env.

## Setup

1) **Create a Hugging Face Write Token**
- https://huggingface.co/settings/tokens → New token (Role: Write).

2) **Repo Settings → Secrets and variables → Actions → New repository secret**
- `HF_TOKEN` → your HF write token
- `MY_API_KEY` → your real app key (e.g., OpenAI key)

3) **Repo Settings → Secrets and variables → Actions → New repository variable**
- `SPACE_ID` → `your-username/your-space-name` (exactly this format)

4) Push to `main` branch.
- The workflow `.github/workflows/deploy.yml` will:
  - Create (if needed) or update your HF Space (SDK: fastapi)
  - Upload code (this folder)
  - Set Space Secret `MY_API_KEY`

## Local files

- `app.py` — FastAPI backend
- `index.html` — Static frontend
- `requirements.txt`, `runtime.txt` — runtime config for HF
- `.github/workflows/deploy.yml` — GitHub Action for CI/CD

## Test

After deploy, open your Space:
`https://huggingface.co/spaces/<SPACE_ID>`

Then click the button on the homepage. It calls `/hello` which uses the secret server-side.
