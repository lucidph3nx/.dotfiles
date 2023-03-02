#!/bin/sh
# open office blinds
curl -X POST \
  -H "Authorization: Bearer ${HASS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "cover.office_blinds"}' \
  https://home-assistant.tinfoilforest.nz/api/services/cover/open_cover
