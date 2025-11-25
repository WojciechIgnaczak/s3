#!/bin/bash
USER="mysqluser"
PASSWORD="mysqlpass"
NAME_DATABASE="mysqldb"
docker exec -t mysql_container mysql -u${USER} -p${PASSWORD} ${NAME_DATABASE} < poll.sql
