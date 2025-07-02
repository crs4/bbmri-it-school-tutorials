# mongo-init/Dockerfile
FROM mongo:latest

# Copia lo script di inizializzazione nella directory Docker di init di MongoDB
# MongoDB eseguirà automaticamente qualsiasi script .js trovato in /docker-entrypoint-initdb.d/
COPY load_biobank_data.js /docker-entrypoint-initdb.d/