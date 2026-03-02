# --------------------------------------------------
# RPA - レイヤー構成 - サービス層
# --------------------------------------------------
class GoogleService:

    def __init__(self, rpa_client):
        self.rpa_client = rpa_client

    def execute(self) -> str:
        self.rpa_client.open_top_page()
        title = self.rpa_client.get_title()
        return title