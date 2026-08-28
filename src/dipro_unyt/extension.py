from unyt import unyt_array as unyt_array_original

class unyt_array(unyt_array_original):
    """Enhanced unyt_array that adds IMAS metadata."""

    def __new__(cls, *args, imas_ids: str = "", description: str = "", species=None, species_idx=None, whatever_property_we_need=None, symbol=None, species_type=None, **kwargs) -> None:
        instance = super().__new__(cls, *args, **kwargs) #TODO: add a clean check of kwargs so the error does not propagate into unyt and scares the users
        instance.imas_ids = imas_ids
        instance.description = description
        instance.species = species
        instance.species_idx = species_idx
        instance.species_type = species_type
        instance.symbol = symbol

        instance.whatever_property_we_need = whatever_property_we_need
        return instance




