@echo off

call C:\Users\DELL\env\Scripts\activate.bat

python C:\Users\DELL\semigod_socials\extraction_scripts\spotify_extraction.py
python C:\Users\DELL\semigod_socials\extraction_scripts\spotify_ingestion.py

cd C:\Users\DELL\semigod_socials\semi
dbt build --profiles-dir .

