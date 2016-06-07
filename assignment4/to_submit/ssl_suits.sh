#!/usr/bin/env bash

servers='top_sites.txt'
suites=$(openssl ciphers 'ALL:eNULL')
suites=${suites//:/ }

while read -r site
do
  echo $site
  for suite in ${suites[@]}
  do
  response=$(echo -n | openssl s_client -cipher "$suite" -connect $site:443 2>&1)
  #echo $response
  if [[ "$response" =~ ":error:" ]] ; then
    error="not supported $suite"
  else 
    if [[ "$response" =~ "Cipher is ${cipher}" || "$response" =~ "Cipher    :" ]] ; then
      echo $suite
      echo $suite >> 'used_suites.txt'
    fi
  fi
  done
done < "$servers"
