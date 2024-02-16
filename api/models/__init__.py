from .poi import PoI
from auditlog.registry import auditlog


__all__ = (
    'PoI',
)

auditlog.register(PoI)