# Backend stage
FROM python:3.9-slim as backend
WORKDIR /usr/src/app/backend
COPY shopping-app-server/requirements.txt .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt
COPY shopping-app-server/ .

# Frontend stage
FROM node:20 as frontend
WORKDIR /app
COPY shopping-app-ui/package.json shopping-app-ui/package-lock.json ./
RUN npm install
COPY shopping-app-ui/ .
RUN npm run build

# Final stage with Nginx
FROM nginx:alpine
RUN apk add --update --no-cache python3 py3-pip && pip3 install gunicorn
COPY --from=frontend /app/dist/shopping-app-ui/browser/ /usr/share/nginx/html
COPY --from=backend /usr/src/app/backend /backend
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY start.sh /start.sh
RUN chmod +x /start.sh
EXPOSE 80 5000
CMD ["/start.sh"]
