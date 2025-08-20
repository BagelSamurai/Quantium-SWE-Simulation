#!/bin/bash

set -e
echo "======================================================"
echo " STARTING TEST RUNNER"
echo "======================================================"

VENV_PATH=".venv/Scripts/activate"

TEST_DIR="frontend"
echo "======================================================"
echo "ACTIVATING VIRTUAL ENVIRONMENT"
echo "======================================================"

if [ ! -f "$VENV_PATH" ]; then
  echo "======================================================"
  echo "ERROR VIRTUAL ENVIRONMENT NOT FOUND AT $VENV_PATH"
  echo "======================================================"
  exit 1
fi
source "$VENV_PATH"

echo "======================================================"
echo "NAVIGATING TO TEST DIRECTORY: $TEST_DIR"
echo "======================================================"
cd "$TEST_DIR"

echo "======================================================"
echo "RUNNING PYTEST...."
pytest
echo "======================================================"

echo "======================================================"
echo "=== TEST SUITE COMPLETED SUCCESSFULLY! "
echo "======================================================"