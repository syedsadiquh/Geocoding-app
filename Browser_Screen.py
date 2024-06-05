import webview

# Browser Window to show the latitude and longitude in browser.
class BrowserWindow:
    def __init__(self, lat, lng):
        webview.create_window('Google Maps', f'https://www.google.com/maps/@?api=1&map_action=map&map_action=map&center={lat}%2C{lng}&zoom=15')
        webview.start()
