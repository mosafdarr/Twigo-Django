#!/bin/bash

#!/bin/bash
# Install npm dependencies
npm install

# Build frontend assets (assuming you have a build script in your package.json)
npm run build

# Build the project
echo "Building the project..."
python3.12 -m pip install -r requirements.txt

# making migrations for databases
echo "Make Migration..."
python3.12 twigo/manage.py makemigrations --noinput
python3.12 twigo/manage.py migrate --noinput

# collecting static files
echo "Collect Static..."
python3.12 twigo/manage.py collectstatic --noinput --clear