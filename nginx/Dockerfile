FROM nginx:1.27.0

# Copy the nginx configuration file and the entrypoint script
COPY nginx.conf.template /etc/nginx/nginx.conf.template
COPY entrypoint.sh /entrypoint.sh

# Create a new user to run the app
RUN mkdir /home/www    
RUN groupadd -r www && useradd -r -g www -d /home/www -s /bin/bash www

# Run the nginx server
# CMD ["nginx", "-g", "daemon off;"]
# Set the correct permissions
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]