#!/bin/sh
# get office temperature
curl -X GET \
  -H "Authorization: Bearer ${HASS_API_KEY}" \
  -H "Content-Type: application/json" \
  https://home-assistant.tinfoilforest.nz/api/states/sensor.office_sensor_temperature \
  | jq -r '.attributes | "\(.temperature) \(.unit_of_measurement)"'

