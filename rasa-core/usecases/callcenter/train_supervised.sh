#!/usr/bin/env bash

python -m rasa_core.train -s stories.md -d domain.yml -o models/policy/init --epochs 500 --history 4 --batch_size 128