#!/bin/bash
# Konfiguracja zmiennych srodowiskowych
CONTAINER_NAME="netflix_postgres_db"
DB_USER="netflixuser"
DB_NAME="netflix"   
BACKUP_DIR="backups"
BACKUP_FILE="${BACKUP_DIR}/backup_$(date +%Y%m%d_%H%M%S).sql"


# wykonaj backup
echo "Tworzenie kopii zapasowej bazy danych ${DB_NAME} z kontenera ${CONTAINER_NAME}..."
docker exec -t ${CONTAINER_NAME} pg_dump -U ${DB_USER} -d ${DB_NAME} > ${BACKUP_FILE}

# kompresowanie pliku backupu
gzip ${BACKUP_FILE}

#sprawdzenie wielkości pliku
BACKUP_SIZE=$(du -h ${BACKUP_FILE}.gz | cut -f1)
echo "Kopia zapasowa utworzona: ${BACKUP_FILE}.gz (o wielkości ${BACKUP_SIZE})"

# usuwanie starych kopii zapasowych
find ${BACKUP_DIR} -type f -name "backup_*.sql.gz" -mtime +7 -exec rm {} \;
echo "Usunięto kopie zapasowe starsze niż 7 dni."
echo "Kopia zapasowa zakończona."