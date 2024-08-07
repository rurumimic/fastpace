#!/usr/bin/env bash

if [ "$1" == "--dev" ]; then
    echo "Installing in development mode..."
    pip install -e . --config-settings editable_mode=strict
else
    echo "Usage: ./install.sh --dev"
fi
