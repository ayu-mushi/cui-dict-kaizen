#!/bin/bash
#w3mなのでインジェクション攻撃の心配はないはず

function echo1() {
  echo "$1"
  echo ""
}

echo1 "Content-type: text/html"

QUERY=$(echo $QUERY_STRING | sed "s/SHARP/\#/g" | sed "s/\,\,/\ /g" | nkf -w --url-input)

echo1 "$QUERY"
