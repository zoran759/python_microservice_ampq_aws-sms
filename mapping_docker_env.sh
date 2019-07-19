#!/usr/bin/env bash

echo ${DEV_AWS_ACCESS_KEY_ID}
sed -e "s/\${AWS_ACCESS_KEY_ID}/${DEV_AWS_ACCESS_KEY_ID}/g;"  ./app/.env.deploy > ./app/.env
