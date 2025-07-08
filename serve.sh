#!/bin/bash

# .env dosyasını yükle
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# Ortam değişkenlerini ayarla
export LANGCHAIN_TRACING_V2=true

# Backend başlat
uvicorn backend.main_graph:app --host 0.0.0.0 --port 7860 --reload
