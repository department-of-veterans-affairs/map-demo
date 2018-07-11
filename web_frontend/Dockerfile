FROM node:4-slim
RUN npm install express
RUN npm install redis
COPY public/ /public/
COPY web_frontend.js /
CMD ["node", "web_frontend.js"]
EXPOSE 80
