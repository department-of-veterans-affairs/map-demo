FROM node:4-slim
RUN npm install express
RUN npm install redis
COPY public/ /public/
COPY web_frontend.js /
CMD ["node", "web_frontend.js"]
EXPOSE 80
HEALTHCHECK \
  --interval=5s --timeout=5s --retries=3 --start-period=10s \
  CMD curl --fail http://localhost/ || exit 1  