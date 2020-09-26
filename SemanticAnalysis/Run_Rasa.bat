@echo off
start cmd /k "activate rasa && cd C:\Rasa && rasa run actions"
start cmd /k "activate rasa && cd C:\Rasa && rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml"