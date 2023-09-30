databases:
  - name: mysite
    databaseName: syfit
    user: ''

services:
  -type: web
    name: mysite
    runtime: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn mysite.wsgi:application"
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: mysite
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: WEB_CONCURRENCY
        value: 4