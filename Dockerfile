FROM ghcr.io/ggerganov/llama.cpp:server--b1-e09a800

RUN apt-get update && apt-get install -y wget pip python3 git 

RUN wget -q https://huggingface.co/Mihaiii/shieldgemma-2b-Q5_K_M-GGUF/resolve/main/shieldgemma-2b-q5_k_m-imat.gguf
RUN wget -q https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q5_K_M.gguf

COPY . .

RUN chmod 777 .

EXPOSE 7860

RUN pip install -r requirements.txt
