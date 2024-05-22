# Discord fxtwitter

Looks at messages on a discord server, and if it spots a x.com or twitter.com URL, it deletes the message, and republishes it with fxtwitter.com

Yes I am that lazy.

## Usage

```py
DISCORD_TOKEN='YOUR_TOKEN_HERE'
python3 ./main.py
```

```bash
docker run --rm -e DISCORD_TOKEN='YOUR_TOKEN_HERE' ghcr.io/gedasfx/discord-fxtwitter:latest
```
