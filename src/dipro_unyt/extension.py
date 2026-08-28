from unyt import unyt_array as unyt_array_original
# Define your enhancements as before
class unyt_array(unyt_array_original):
    """Enhanced unyt_array that adds IMAS metadata."""

    # def __init__(self, *args, imas_leaf: str = "", description: str = "", species=None, species_idx=None, whatever_property_we_need=None, **kwargs) -> None:
    #     self.imas_leaf = imas_leaf
    #     self.description = description
    #     self.species = species
    #     self.species_idx = species_idx
    #     self.whatever_property_we_need = whatever_property_we_need
    #     super().__init__(*args, **kwargs)

    def __new__(cls, *args, imas_ids: str = "", description: str = "", species=None, species_idx=None, whatever_property_we_need=None, **kwargs) -> None:
        instance = super().__new__(cls, *args, **kwargs)
        instance.imas_ids = imas_ids
        instance.description = description
        instance.species = species
        instance.species_idx = species_idx
        instance.species_type = None
        instance.symbol = None
        instance.species_type = None

        instance.whatever_property_we_need = whatever_property_we_need
        return instance




