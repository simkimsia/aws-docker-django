## Common Nginx Configuration
read -r -d '' FILECONTENT <<'ENDFILECONTENT'


ENDFILECONTENT

echo "$FILECONTENT" > /etc/nginx/common.conf
 
## FastCGI Configuration
read -r -d '' FILECONTENT <<'ENDFILECONTENT'
fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;

fastcgi_param  QUERY_STRING       $query_string;
fastcgi_param  REQUEST_METHOD     $request_method;
fastcgi_param  CONTENT_TYPE       $content_type;
fastcgi_param  CONTENT_LENGTH     $content_length;

fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
fastcgi_param  REQUEST_URI        $request_uri;
fastcgi_param  DOCUMENT_URI       $document_uri;
fastcgi_param  DOCUMENT_ROOT      $document_root;
fastcgi_param  SERVER_PROTOCOL    $server_protocol;

fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;

fastcgi_param  REMOTE_ADDR        $remote_addr;
fastcgi_param  REMOTE_PORT        $remote_port;
fastcgi_param  SERVER_ADDR        $server_addr;
fastcgi_param  SERVER_PORT        $server_port;
fastcgi_param  SERVER_NAME        $server_name;
fastcgi_param  HTTPS              $ssl_session_id;

fastcgi_index  index.php;

# PHP only, required if PHP was built with --enable-force-cgi-redirect
fastcgi_param  REDIRECT_STATUS    200;

fastcgi_connect_timeout 60;
fastcgi_read_timeout 180;
fastcgi_send_timeout 180;

fastcgi_buffer_size 128k;
fastcgi_buffers 4 256k;
fastcgi_busy_buffers_size 256k;
fastcgi_temp_file_write_size 256k;
fastcgi_intercept_errors on;

ENDFILECONTENT
echo "$FILECONTENT" > /etc/nginx/fastcgi_params
 
## Nginx Main Configuration
read -r -d '' FILECONTENT <<'ENDFILECONTENT'
user www-data;
worker_processes 4;
pid /var/run/nginx.pid;

events {
	worker_connections 768;
}

http {
	sendfile off; #sendfile deliberately turn off
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 2;
	types_hash_max_size 2048;
	include /etc/nginx/mime.types;
	default_type application/octet-stream;
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;
	gzip on;
	gzip_disable "msie6";
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}

ENDFILECONTENT
echo "$FILECONTENT" > /etc/nginx/nginx.conf
 
## PHP Configuration
read -r -d '' FILECONTENT <<'ENDFILECONTENT'
location ~ \.php$ {
	fastcgi_pass 127.0.0.1:9000;
	include fastcgi_params;
}

index index.php;

ENDFILECONTENT
echo "$FILECONTENT" > /etc/nginx/php.conf
 
## Default Site Configuration
read -r -d '' FILECONTENT <<'ENDFILECONTENT'
server {
	listen   80; ## listen for ipv4; this line is default and implied
	root /usr/share/nginx/www;
	index index.html index.htm;
	server_name localhost;

	location / {
		try_files $uri $uri/ /index.html;
	}

	location /doc {
		root /usr/share;
		autoindex on;
		allow 127.0.0.1;
		deny all;
	}

	location /images {
		root /usr/share;
		autoindex off;
	}
}

ENDFILECONTENT
echo "$FILECONTENT" > /etc/nginx/sites-available/default