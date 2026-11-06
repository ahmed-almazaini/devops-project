#!/bin/bash

echo "Checking /health..."
curl -f http://localhost:5000/health

echo
echo "Checking /contact..."
curl -f http://localhost:5000/contact

echo
echo "Service verification completed."
