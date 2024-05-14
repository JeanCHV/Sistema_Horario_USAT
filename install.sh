#!/bin/bash

# Crea un entorno virtual
py -3 -m venv .venv

# Activa el entorno virtual
source .venv/bin/activate

# Instala los requisitos del archivo requirements.txt
pip install -r requirements.txt
