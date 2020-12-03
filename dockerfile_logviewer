FROM gorialis/discord.py:master

WORKDIR /app
ADD ./logviewer /app

EXPOSE 8880/tcp

RUN pip install -r requirements.txt

CMD ["python", "app.py"]