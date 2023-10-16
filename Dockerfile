# Используем официальный образ PostgreSQL
FROM postgres:latest

# Создаем базу данных, пользователя и пароль
ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword1234

EXPOSE 5432