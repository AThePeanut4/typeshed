import datetime
from typing import ClassVar, Final

from ..core import WesternCalendar

class Brazil(WesternCalendar):
    """Brazil"""
    include_sao_jose: ClassVar[bool]
    sao_jose_label: ClassVar[str]
    include_sao_pedro: ClassVar[bool]
    sao_pedro_label: ClassVar[str]
    include_sao_joao: ClassVar[bool]
    sao_joao_label: ClassVar[str]
    include_servidor_publico: ClassVar[bool]
    servidor_publico_label: ClassVar[str]
    include_consciencia_negra: ClassVar[bool]
    consciencia_negra_day: ClassVar[tuple[int, int]]
    consciencia_negra_label: ClassVar[str]

class BrazilAcre(Brazil):
    """Brazil Acre State"""
    ...
class BrazilAlagoas(Brazil):
    """Brazil Alagoas State"""
    ...
class BrazilAmapa(Brazil):
    """Brazil Amapá State"""
    ...
class BrazilAmazonas(Brazil):
    """Brazil Amazonas State"""
    ...
class BrazilBahia(Brazil):
    """Brazil Bahia State"""
    ...
class BrazilCeara(Brazil):
    """Brazil Ceará State"""
    ...
class BrazilDistritoFederal(Brazil):
    """Brazil Distrito Federal State"""
    ...
class BrazilEspiritoSanto(Brazil):
    """Brazil Espírito Santo State"""
    ...
class BrazilGoias(Brazil):
    """Brazil Goiás State"""
    ...
class BrazilMaranhao(Brazil):
    """Brazil Maranhão State"""
    ...
class BrazilMinasGerais(Brazil):
    """Brasil Minas Gerais State"""
    ...
class BrazilMatoGrosso(Brazil):
    """Brazil Mato Grosso State"""
    ...
class BrazilMatoGrossoDoSul(Brazil):
    """Brazil Mato Grosso do Sul State"""
    ...
class BrazilPara(Brazil):
    """Brazil Pará State"""
    ...
class BrazilParaiba(Brazil):
    """Brazil Paraíba State"""
    ...
class BrazilPernambuco(Brazil):
    """Brazil Pernambuco State"""
    ...
class BrazilPiaui(Brazil):
    """Brazil Piauí State"""
    ...
class BrazilParana(Brazil):
    """Brazil Paraná State"""
    ...

class BrazilRioDeJaneiro(Brazil):
    """Brazil Rio de Janeiro State"""
    fat_tuesday_label: ClassVar[str]
    def get_dia_do_comercio(self, year: int) -> datetime.date | None:
        """
        Return Dia do Comércio variable date

        It happens on the 3rd Monday of october.
        """
        ...

class BrazilRioGrandeDoNorte(Brazil):
    """Brazil Rio Grande do Norte State"""
    ...
class BrazilRioGrandeDoSul(Brazil):
    """Brazil Rio Grande do Sul State"""
    ...
class BrazilRondonia(Brazil):
    """Brazil Rondônia State"""
    ...
class BrazilRoraima(Brazil):
    """Brazil Roraima State"""
    ...
class BrazilSantaCatarina(Brazil):
    """Brazil Santa Catarina State"""
    ...
class BrazilSaoPauloState(Brazil):
    """Brazil São Paulo State"""
    ...

class BrazilSaoPauloCity(BrazilSaoPauloState):
    """Brazil São Paulo City"""
    fat_tuesday_label: ClassVar[str]

class BrazilSergipe(Brazil):
    """Brazil Sergipe State"""
    ...
class BrazilTocantins(Brazil):
    """Brazil Tocantins State"""
    ...
class BrazilVitoriaCity(BrazilEspiritoSanto):
    """Brazil Vitória City"""
    ...
class BrazilVilaVelhaCity(BrazilEspiritoSanto):
    """Brazil Vila Velha City"""
    ...
class BrazilCariacicaCity(BrazilEspiritoSanto):
    """Brazil Cariacica City"""
    ...
class BrazilGuarapariCity(BrazilEspiritoSanto):
    """Brazil Guarapari City"""
    ...

class BrazilSerraCity(BrazilEspiritoSanto):
    """Brazil Serra City"""
    fat_tuesday_label: ClassVar[str]

class BrazilRioBrancoCity(BrazilAcre):
    """Brazil Rio Branco City"""
    ...
class BrazilMaceioCity(BrazilAlagoas):
    """Brazil Maceió City"""
    ...
class BrazilManausCity(BrazilAmazonas):
    """Brazil Manaus City"""
    ...
class BrazilMacapaCity(BrazilAmapa):
    """Brazil Macapá City"""
    ...
class BrazilSalvadorCity(BrazilBahia):
    """Brazil Salvador City"""
    ...
class BrazilFortalezaCity(BrazilCeara):
    """Brazil Fortaleza City"""
    ...
class BrazilGoianiaCity(BrazilGoias):
    """Brazil Goiânia City"""
    ...
class BrazilBeloHorizonteCity(BrazilMinasGerais):
    """Brazil Belo Horizonte City"""
    ...
class BrazilCampoGrandeCity(BrazilMatoGrossoDoSul):
    """Brazil Campo Grande City"""
    ...
class BrazilCuiabaCity(BrazilMatoGrosso):
    """Brazil Cuiabá City"""
    ...
class BrazilBelemCity(BrazilPara):
    """Brazil Belém City"""
    ...
class BrazilJoaoPessoaCity(BrazilParaiba):
    """Brazil João Pessoa City"""
    ...
class BrazilRecifeCity(BrazilPernambuco):
    """Brazil Recife City"""
    ...
class BrazilTeresinaCity(BrazilPiaui):
    """Brazil Teresina City"""
    ...
class BrazilCuritibaCity(BrazilParana):
    """Brazil Curitiba City"""
    ...
class BrazilNatalCity(BrazilRioGrandeDoNorte):
    """Brazil Natal City"""
    ...
class BrazilPortoVelhoCity(BrazilRondonia):
    """Brazil Porto Velho City"""
    ...
class BrazilBoaVistaCity(BrazilRoraima):
    """Brazil Boa Vista City"""
    ...
class BrazilPortoAlegreCity(BrazilRioGrandeDoSul):
    """Brazil Porto Alegre City"""
    ...
class BrazilChapecoCity(BrazilSantaCatarina):
    """Brazil Chapecó City"""
    ...
class BrazilFlorianopolisCity(BrazilSantaCatarina):
    """Brazil Florianópolis City"""
    ...
class BrazilJoinvilleCity(BrazilSantaCatarina):
    """Brazil Joinville City"""
    ...
class BrazilAracajuCity(BrazilSergipe):
    """Brazil Aracaju City"""
    ...
class BrazilSorocabaCity(BrazilSaoPauloState):
    """Brazil Sorocaba City"""
    ...
class BrazilPalmasCity(BrazilTocantins):
    """Brazil Palmas City"""
    ...

class BrazilBankCalendar(Brazil):
    """
    Calendar that considers only working days for bank transactions
    for companies and the general public
    """
    fat_tuesday_label: ClassVar[str]
    def get_last_day_of_year_for_only_internal_bank_trans(self, year: int) -> datetime.date:
        """
        The last day of year isn't a working day for public bank
        transactions in Brazil. More details can be read in
        http://www.bcb.gov.br/pre/bc_atende/port/servicos4.asp
        """
        ...

IBGE_TUPLE: Final[tuple[tuple[str, type[Brazil]], ...]]
IBGE_REGISTER: Final[dict[str, type[Brazil]]]
