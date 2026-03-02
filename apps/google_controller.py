from apps.google_rpa_client import GoogleRpaClient
from apps.google_service import GoogleService

# --------------------------------------------------
# RPA - レイヤー構成 - コントローラ層
# --------------------------------------------------
def run():
    client = GoogleRpaClient(headless=True)
    service = GoogleService(client)

    title = service.execute()
    print(title)

    client.close()
