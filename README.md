SANSKRITI CANVAS - FINAL PROTOTYPE PACKAGE
===========================================

Project flow:
Home -> Explore India -> State -> District/City -> Heritage/Culture -> Details

Public browsing does not require login. Login/Register is required only when contributing hidden/local heritage.
Contribution flow: Share Hidden Heritage -> Login/Register -> Submit -> Admin Review -> Approve/Reject.

IMPORTANT IMAGE SYSTEM
----------------------
Fixed paths have been prepared for Gujarat district previews and major state previews.
See IMAGE_REQUIREMENTS.txt for the exact filename list.

The current districts/ and states/ folders contain temporary prototype copies so no image path is broken. Replace each temporary file with the final realistic photograph using the exact same filename. No code change is required for image replacement.

Core pages:
index.html
explore.html
gujarat.html
ahmedabad.html
heritage.html
heritage-detail.html
culture.html
food.html
festivals.html
search.html
login.html
register.html
contribute.html
admin.html

Backend foundation:
backend/app.py
backend/requirements.txt
backend/schema.sql

Note: the current Flask backend is a prototype foundation with in-memory demo data. MySQL persistence/authentication still needs to be connected for a production-ready SIH build.

Map data currently loads from external GeoJSON/ArcGIS services, so an internet connection is required for map rendering.
