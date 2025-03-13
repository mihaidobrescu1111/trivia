FROM python:3.10

WORKDIR /trivia-app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 7860

ARG HF_CLIENT_ID
ARG HF_CLIENT_SECRET
ARG HF_REDIRECT_URI
ARG GOOGLE_CLIENT_ID
ARG GOOGLE_CLIENT_SECRET
ARG GOOGLE_REDIRECT_URI

ENV HF_CLIENT_ID=$HF_CLIENT_ID
ENV HF_CLIENT_SECRET=$HF_CLIENT_SECRET
ENV HF_REDIRECT_URI=$HF_REDIRECT_URI
ENV GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID
ENV GOOGLE_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET
ENV GOOGLE_REDIRECT_URI=$GOOGLE_REDIRECT_URI
ENV DB_DIRECTORY=/app/db