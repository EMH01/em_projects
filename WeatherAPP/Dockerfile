# Stage builder: installing dependencies
FROM python:3.12 AS builder 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage to copy files and be reade to start
FROM python:3.12

# user not roort
RUN useradd -m anyuser
USER anyuser

WORKDIR /app

COPY --from=builder /app /app
COPY . .

