# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app
Run pip3 install --upgrade pip
Run pip3 install GoogleNews
Run pip3 install newspaper3k
Run pip3 install validators
Run pip3 install transformers
Run pip3 install sentence_transformers
Run pip3 install rouge

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]