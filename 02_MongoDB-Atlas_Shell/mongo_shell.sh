#!/bin/bash

echo "Atlas sh"
echo ""
echo "Atlas user? :  "
read user
echo "Atlas Pass? : "
read -s password
echo "Full mongodb:// URI? : "
read uri


mongosh "$uri" --apiVersion 1 --tls --authenticationDatabase admin --username "$user" --password "$password"