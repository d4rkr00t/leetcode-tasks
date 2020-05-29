#!/usr/bin/env bash

function pick {
  FILE="$(find ./tasks -type f | shuf -n 1 | sed -e 's/.\/tasks\///')"

  if [ -f "./solutions/$FILE" ];
  then
      echo "$FILE exist"
      pick
  else
    cp "./tasks/$FILE" "./solutions/$FILE"
    echo "Next tasks: $FILE"
  fi
}

pick
