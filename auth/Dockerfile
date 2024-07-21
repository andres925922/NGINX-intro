FROM python:3.12

# Copy the current directory contents into the container at /app
COPY . /app

# Create a new user to run the app
RUN mkdir /home/fastapi-user    
RUN groupadd -r fastapi-group && useradd -r -g fastapi-group -d /home/fastapi-user -s /bin/bash fastapi-user

# Change ownership and permissions before switching user
RUN chown -R fastapi-user:fastapi-group /home/fastapi-user /app && chmod u+x /app/gunicorn

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run gunicorn with the app
# CMD ["tail", "-f", "/dev/null"]
CMD ["./gunicorn"]
