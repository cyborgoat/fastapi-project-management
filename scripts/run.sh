#!/bin/sh

set -e

uvicorn main:app --proxy-headers --host 0.0.0.0 --port 80