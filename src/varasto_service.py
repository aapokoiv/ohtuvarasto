from varasto import Varasto


class VarastoService:
    def __init__(self):
        self._varastot = {}
        self._seuraava_id = 1

    def luo_varasto(self, nimi, tilavuus, alku_saldo=0):
        varasto_id = self._seuraava_id
        self._seuraava_id += 1
        self._varastot[varasto_id] = {
            "nimi": nimi,
            "varasto": Varasto(tilavuus, alku_saldo)
        }
        return varasto_id

    def hae_varasto(self, varasto_id):
        return self._varastot.get(varasto_id)

    def hae_kaikki_varastot(self):
        return self._varastot

    def lisaa_varastoon(self, varasto_id, maara):
        varasto_data = self._varastot.get(varasto_id)
        if varasto_data:
            varasto_data["varasto"].lisaa_varastoon(maara)
            return True
        return False

    def ota_varastosta(self, varasto_id, maara):
        varasto_data = self._varastot.get(varasto_id)
        if varasto_data:
            return varasto_data["varasto"].ota_varastosta(maara)
        return 0
