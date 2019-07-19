#!/usr/bin/env bash

echo ${DEV_AWS_ACCESS_KEY_ID}
sed -e "s/\${AWS_ACCESS_KEY_ID}/${DEV_AWS_ACCESS_KEY_ID}/g;
         s/\${AWS_SECRET_ACCESS_KEY}/${DEV_AWS_SECRET_ACCESS_KEY}/g;
         s/\${AWS_DEFAULT_REGION}/${DEV_AWS_DEFAULT_REGION}/g;"  ./app/.env.deploy > ./app/.env
