# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for static and media files
RUN mkdir -p /app/staticfiles /app/media

# Copy the entire Django project into the container
COPY . /app/

# Run collectstatic and migrate
RUN python manage.py collectstatic --no-input && python manage.py migrate

# Expose the port the app runs on
EXPOSE 8010

# Start the Django server
CMD ["gunicorn", "--config", "conf/gunicorn.conf.py", "ecom.wsgi", "--preload"]
