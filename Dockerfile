# Dockerfile pour StartupAI - Epic 11: Investisseur IA
FROM python:3.9-slim

# Métadonnées
LABEL maintainer="StartupAI Team"
LABEL version="1.0.0"
LABEL description="Système d'investissement IA pour startups"

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV ENV=production
ENV DEBUG=false

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Création du répertoire de travail
WORKDIR /app

# Copie des fichiers de dépendances
COPY core-engine/requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY core-engine/ ./core-engine/
COPY frontend/build/ ./frontend/build/

# Création de l'utilisateur non-root
RUN useradd --create-home --shell /bin/bash startupai && \
    chown -R startupai:startupai /app

# Changement vers l'utilisateur non-root
USER startupai

# Exposition du port
EXPOSE 8000

# Script de démarrage
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Point d'entrée
ENTRYPOINT ["docker-entrypoint.sh"]

# Commande par défaut
CMD ["uvicorn", "core-engine.api:app", "--host", "0.0.0.0", "--port", "8000"]