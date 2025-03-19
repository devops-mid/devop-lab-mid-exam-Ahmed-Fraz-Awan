#!/bin/bash
echo "Running unit tests..."
pytest test_app.py -v
echo "Running integration tests..."
pytest test_integration.py -v
echo "Tests completed."