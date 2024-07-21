FROM nginx:1.27.0

# Copy the nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf
COPY snippets /etc/nginx/snippets

# Create a new user to run the app
RUN mkdir /home/www    
RUN groupadd -r www && useradd -r -g www -d /home/www -s /bin/bash www

# Run the nginx server
CMD ["nginx", "-g", "daemon off;"]