# Start from python slim-buster docker image
FROM python:3.9-slim-buster

# Update base packages
RUN apt-get update
RUN apt-get upgrade -y

# Copy files to working directory
COPY ./src/ /app/src/
WORKDIR /app/src

# Install python packages using requirements.txt
RUN pip install -r requirements.txt

# Run the script
CMD python app.py