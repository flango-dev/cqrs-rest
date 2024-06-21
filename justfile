default:
  just --list

# setup venv
venv-setup:
  scripts/setup_venv.sh

# setup local database
database-setup-local:
  scripts/setup_database.sh

# setup project
project-setup: venv-setup database-setup-local

# run project using granian wsgi server
project-run:
  granian --interface wsgi --reload demo.wsgi:application
