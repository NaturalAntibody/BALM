from .modeling_balm import BALMForMaskedLM
from .ba_position_embedding import get_anarci_pos

__all__ = ["BALMForMaskedLM", "get_anarci_pos"]

def get_vocab_path():
    """Returns the absolute path to the bundled vocab.txt file."""
    try:
        from importlib import resources
        # Python 3.9+ way to access resources
        return resources.files("balm.tokenizer").joinpath("vocab.txt")
    except (ImportError, AttributeError):
        # Fallback for older environments or if not installed as a package
        import os
        return os.path.join(os.path.dirname(__file__), "tokenizer", "vocab.txt")
