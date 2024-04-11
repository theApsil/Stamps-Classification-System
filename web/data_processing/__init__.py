from web.data_processing.classification import classify
from web.data_processing.data import read_json_file, fix_data_ranges, get_combox_values
from web.data_processing.update_data import add_attribute, delete_attribute, change_attribute_value
from web.data_processing.update_classes import remove_class_from_json, change_class_name

__all__ = [
    "get_combox_values",
    "classify",
    "read_json_file",
    "fix_data_ranges",
    "add_attribute",
    "delete_attribute",
    "change_attribute_value",
    "remove_class_from_json",
    "change_class_name"
]
