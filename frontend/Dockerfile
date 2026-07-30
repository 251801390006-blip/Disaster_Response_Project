
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose Vite default port
EXPOSE 5173

# Command to run the application in dev mode
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

