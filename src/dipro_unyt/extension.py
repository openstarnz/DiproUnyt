from unyt import unyt_array as unyt_array_original
from unyt import unyt_quantity as unyt_quantity_original

class unyt_array(unyt_array_original):
    """Enhanced unyt_array that adds IMAS metadata."""

    def __new__(cls, 
            input_array,
            units=None,
            registry=None,
            dtype=None,
            *,
            bypass_validation=False,
            name=None,
            imas_ids: str = "",
            description: str = "",
            species=None,
            species_idx=None,
            whatever_property_we_need=None,
            symbol=None,
            species_type=None,
            ) -> None:
        instance = super().__new__(
        cls,
        input_array,
        units=units,
        registry=registry,
        dtype=dtype,
        bypass_validation=bypass_validation,
        name=name,
    ) 
        instance.imas_ids = imas_ids
        instance.description = description
        instance.species = species
        instance.species_idx = species_idx
        instance.species_type = species_type
        instance.symbol = symbol

        instance.whatever_property_we_need = whatever_property_we_need
        return instance

class unyt_quantity(unyt_quantity_original):
    """Enhanced unyt_quantity that adds IMAS metadata."""

    def __new__(cls, 
            input_scalar,
            units=None,
            registry=None,
            dtype=None,
            *,
            bypass_validation=False,
            name=None,
            imas_ids: str = "",
            description: str = "",
            species=None,
            species_idx=None,
            whatever_property_we_need=None,
            symbol=None,
            species_type=None,
            ) -> None:
        instance = super().__new__(
        cls,
        input_scalar,
        units=units,
        registry=registry,
        dtype=dtype,
        bypass_validation=bypass_validation,
        name=name,
    ) 
        instance.imas_ids = imas_ids
        instance.description = description
        instance.species = species
        instance.species_idx = species_idx
        instance.species_type = species_type
        instance.symbol = symbol

        instance.whatever_property_we_need = whatever_property_we_need
        return instance




