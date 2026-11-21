FROM python:3.12-slim

# uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Dépendances
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# Dossiers de code
COPY src ./src
COPY Models ./Models

# Utiliser le venv créé par uv
ENV PATH="/app/.venv/bin:$PATH"

# Execution du serveur uvicorn
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]