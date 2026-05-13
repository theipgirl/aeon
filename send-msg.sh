#!/usr/bin/env bash
set -euo pipefail
MSG=$(cat daily-routine-msg.md)
./notify "$MSG"
