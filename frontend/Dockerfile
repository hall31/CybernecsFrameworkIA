# Dockerfile pour le frontend React de StartupAI
FROM node:18-alpine as build

# Métadonnées
LABEL maintainer="StartupAI Team"
LABEL version="1.0.0"
LABEL description="Frontend React pour le système d'investissement IA"

# Répertoire de travail
WORKDIR /app

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation des dépendances
RUN npm ci --only=production

# Copie du code source
COPY . .

# Build de l'application
RUN npm run build

# Stage de production avec Nginx
FROM nginx:alpine

# Copie des fichiers buildés
COPY --from=build /app/build /usr/share/nginx/html

# Copie de la configuration Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Exposition du port
EXPOSE 3000

# Démarrage de Nginx
CMD ["nginx", "-g", "daemon off;"]