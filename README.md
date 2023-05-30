# netbox-api Tests

Small pynetbox scripts to play with Netbox API

## Netbox DEV - Feed with StepStone data
- Get postgres dump and media files backup from StepStone
- Restore with following commands :  

  ```sh
  # Postgres Data
  docker compose exec -T postgres sh -c 'pg_restore -v -Fc -c -U $POSTGRES_USER -d $POSTGRES_DB' < "postgres.pgdump"
  
  # Media Files
  docker compose exec -u root -T netbox tar x -zvf - -C /opt/netbox/netbox/media < "media.tgz"
  ```
- If you need to change the admin account password :
    ```sh
    docker compose exec -it netbox /bin/bash
    $ ./manage.py changepassword admin
    ```
