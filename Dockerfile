# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the entire Django project into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8010

# Start the Django server
CMD python manage.py collectstatic --no-input && python manage.py migrate && gunicorn --config conf/gunicorn.conf.py ecom.wsgi --preload
