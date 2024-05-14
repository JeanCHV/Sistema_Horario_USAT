#!/bin/bash

# Crea un entorno virtual
py -3 -m venv .venv

# Espera un segundo
sleep 1

# Activa el entorno virtual
source .venv/bin/activate

# Espera un segundo
sleep 1

# Instala los requisitos del archivo requirements.txt
pip install -r requirements.txt
