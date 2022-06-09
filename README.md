# Condominios-api
Aplicación web para el ramo de integración de sistemas 

## MySql
User: USER_API

User_Pass: user_api_admin

```sql
CREATE USER 'USER_API'@'%' IDENTIFIED VIA mysql_native_password USING '***';
GRANT ALL PRIVILEGES ON *.* TO 'USER_API'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
```

DB: API_REST