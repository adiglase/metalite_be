#!/bin/bash
WORKING_DIR=$(dirname "$PWD")

touch .env

{
  echo "# MySql Env Variables"
  echo MYSQL_USER=mysql_admin
  echo MYSQL_PASSWORD=admin
  echo MYSQL_PORT=5432
  echo MYSQL_HOST=db
  echo MYSQL_DATABASE=metalite_db
  echo MYSQL_ROOT_PASSWORD=admin

  echo PMA_HOST=db
  echo

  echo "# Django allowed client host access"
  echo ALLOWED_HOST=localhost
  echo
  echo "# Working directories"
  echo BACKEND_WORKING_DIR="$WORKING_DIR/metalite_be"
  echo FRONTEND_WORKING_DIR="$WORKING_DIR/metalite_fe"
} > .env

echo ".env file has been created."
