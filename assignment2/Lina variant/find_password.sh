#!/bin/bash
# echo `java MD5Crypt -apache netsec16 XBN4ZxSl`
# echo `openssl passwd -apr1 -salt XBN4ZxSl netsec16`

text=$(curl -s https://tools.ietf.org/rfc/rfc3093.txt)
password=""

for word in $text; do
  echo -ne '.'
  #encrypted=`java MD5Crypt -apache $word /pE9u4cQ`
  encrypted=`openssl passwd -apr1 -salt /pE9u4cQ $word 2>/dev/null`

  if [ "$encrypted" = "\$apr1$/pE9u4cQ\$ZfQfXfZ8NWh2gfFpIx22T0" ];
    then
      password=$word;
  fi;
done

echo ""
echo "===========RESULT==========="
echo $password
echo `openssl passwd -apr1 -salt /pE9u4cQ $password`
