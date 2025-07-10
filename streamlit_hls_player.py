import streamlit.components.v1 as components

def hls_player(m3u8_url: str, width=700, height=400):
    player_code = f"""
    <html>
    <head>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    </head>
    <body>
    <video id="video" controls autoplay width="{width}" height="{height}" style="border:1px solid #ccc"></video>
    <script>
      var video = document.getElementById('video');
      if(Hls.isSupported()) {{
        var hls = new Hls();
        hls.loadSource("{m3u8_url}");
        hls.attachMedia(video);
      }} else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
        video.src = "{m3u8_url}";
      }}
    </script>
    </body>
    </html>
    """
    components.html(player_code, height=height + 50)
