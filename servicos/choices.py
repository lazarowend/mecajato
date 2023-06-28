from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCA_DE_OLEO = 'TDO', 'Troca de óleo'
    TROCAS_DE_PNEUS = 'TDP', 'Troca de pneus'
    BALANCEAMENTO = 'B', 'Balanceamento'
    SERVICOS = 'SDF', 'Serviço de freios'
    TROCA_DE_CORREIAS = 'TDC', 'Troca de correias'
    REPARO_SISTEMA_DE_ESPACPE = 'RSE', 'Reparo do sistema de escape'
    SUSPENSÃO = 'S', 'Suspensão'
    TROCA_DE_BATERIA = 'TB', 'Troca de bateria'