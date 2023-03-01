FROM python:3.9.2-slim-buster
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install libgl1
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
CMD ["bash","bash.sh"]
