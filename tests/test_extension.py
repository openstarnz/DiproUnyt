"""Tests for the dipro_unyt.extension shim over unyt.unyt_array.

Importing dipro_unyt mounts a merged module onto sys.modules["unyt"] via
modshim, so `unyt.unyt_array` below refers to dipro_unyt.extension.unyt_array,
not the original unyt.unyt_array.
"""

import numpy as np
import pytest

import dipro_unyt  # noqa: F401  (import registers the modshim mount) -> if you remove that line, it breaks as expected!!
import unyt
from unyt.array import unyt_array as original_unyt_array


def test_shim_mounts_extended_class():
    assert issubclass(unyt.unyt_array, original_unyt_array)


def test_imas_metadata_defaults_are_empty():
    a = unyt.unyt_array([1, 2, 3], "m")

    assert a.imas_ids == ""
    assert a.description == ""
    assert a.species is None
    assert a.species_idx is None
    assert a.species_type is None
    assert a.symbol is None
    assert a.whatever_property_we_need is None


def test_imas_metadata_is_stored():
    a = unyt.unyt_array(
        [1, 2, 3],
        "m",
        imas_ids="core_profiles",
        description="electron density",
        species="electron",
        species_idx=0,
        species_type="thermal",
        symbol="n_e",
        whatever_property_we_need="value",
    )

    assert a.imas_ids == "core_profiles"
    assert a.description == "electron density"
    assert a.species == "electron"
    assert a.species_idx == 0
    assert a.species_type == "thermal"
    assert a.symbol == "n_e"
    assert a.whatever_property_we_need == "value"


def test_unyt_array_still_behaves_like_original():
    a = unyt.unyt_array([1, 2, 3], "m", imas_ids="ids1")
    b = unyt.unyt_array([1, 1, 1], "m")

    result = a + b

    np.testing.assert_array_equal(result.to_value("m"), [2, 3, 4])
    assert str(a.units) == "m"


def test_unexpected_kwarg_raises_typeerror():
    with pytest.raises(TypeError):
        unyt.unyt_array([1, 2, 3], "m", not_a_real_kwarg="oops")

def run_tests():
    test_shim_mounts_extended_class()
    test_imas_metadata_defaults_are_empty()
    test_imas_metadata_is_stored()
    test_unyt_array_still_behaves_like_original()
    test_unexpected_kwarg_raises_typeerror()
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()