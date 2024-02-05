# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install django
RUN pip install whitenoise
RUN pip install django-prometheus

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV SECRET_KEY "django-insecure-(j=*vhq55rack966j3m+m5cdbnvg)^n2%*ysmidn$i!&3n+j3s"

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
