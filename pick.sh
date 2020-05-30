#!/usr/bin/env bash

function pick {
  FILE="$(find ./tasks -type f | shuf -n 1 | sed -e 's/.\/tasks\///')"
  NUM="$(echo $FILE | sed -e 's/[^0-9]//g')"

  if [ -f "./solutions/$FILE" ];
  then
      echo "$FILE exist"
      pick
  else
    cp "./tasks/$FILE" "./solutions/$FILE"
    echo -e "✅❌ $NUM\n$(cat solutions.md)" > solutions.md
    echo "Next tasks: $FILE"
  fi
}

pick
